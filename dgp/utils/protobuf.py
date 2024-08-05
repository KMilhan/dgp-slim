# Copyright 2021-2022 Toyota Research Institute.  All rights reserved.
import hashlib
import json
import logging
import os
from io import StringIO
from pathlib import Path

from google.protobuf.json_format import MessageToDict, Parse

from dgp.proto.dataset_pb2 import Ontology as OntologyV1Pb2
from dgp.proto.ontology_pb2 import FeatureOntology as FeatureOntologyPb2
from dgp.proto.ontology_pb2 import Ontology as OntologyV2Pb2

logger = logging.getLogger(__name__)


def parse_pbobject(source, pb_class):
    """Like open_pboject but source can be a path or a bytestring.

    Parameters
    ----------
    source: str or bytes
        Local JSON file path, remote s3 path to object, or bytestring of serialized object

    pb_class: type
        Protobuf pb2 object we want to load into.

    Returns
    -------
    pb_object: pb2 object or None
        Desired pb2 ojbect to be parsed or None if loading fails

    """
    base_message = pb_class()
    if isinstance(source, str):
        return Parse(source, base_message)
    elif isinstance(source, bytes):
        return Parse(source.decode(), base_message)
    else:
        logger.error(f"cannot parse type {type(source)}")

def save_pbobject_as_json(pb_object, save_path):
    """Save protobuf (pb2) object to JSON file with our standard indent, key ordering, and other
    settings.

    Any calls to save protobuf objects to JSON in this repository should be through this function.

    Parameters
    ----------
    pb_object: object
        Protobuf pb2 object we want to save to file

    save_path: str
        If save path is a JSON, serialized object is saved to that path. If save path is directory,
        the `pb_object` is saved in <save_path>/<pb_object_sha>.json.

    Returns
    -------
    save_path: str
        Returns path to saved pb_object JSON

    """
    if os.path.isdir(save_path):
        save_path = os.path.join(
            save_path, generate_uid_from_pbobject(pb_object) + ".json"
        )

    assert save_path.endswith(
        ".json"
    ), "File extension for {} needs to be json.".format(save_path)
    with open(save_path, "w", encoding="UTF-8") as _f:
        json.dump(
            MessageToDict(
                pb_object,
                including_default_value_fields=True,
                preserving_proto_field_name=True,
            ),
            _f,
            indent=2,
            sort_keys=True,
        )
    return save_path


def open_ontology_pbobject(ontology_file):
    """Open ontology objects, first attempt to open V2 before trying V1.

    Parameters
    ----------
    ontology_file: str or bytes
        JSON ontology file path to load or bytestring.

    Returns
    -------
    ontology: Ontology object
        Desired Ontology pb2 object to be opened (either V2 or V1). Returns
        None if neither fails to load.

    """
    try:
        ontology = parse_pbobject(ontology_file, OntologyV2Pb2)
        if ontology is not None:
            logger.debug("Successfully loaded Ontology V2 spec.")
            return ontology
    except Exception:
        logger.error("Failed to load ontology file with V2 spec, trying V1 spec.")
    try:
        ontology = parse_pbobject(ontology_file, OntologyV1Pb2)
        if ontology is not None:
            logger.debug("Successfully loaded Ontology V1 spec.")
            return ontology
    except Exception:
        if isinstance(ontology_file, str):
            logger.error(
                "Failed to load ontology file"
                + ontology_file
                + "with V1 spec also, returning None."
            )
        else:
            logger.error(
                "Failed to load ontology file with V1 spec also, returning None."
            )


def open_feature_ontology_pbobject(ontology_file):
    """Open feature ontology objects.

    Parameters
    ----------
    ontology_file: str
        JSON ontology file path to load.

    Returns
    -------
    ontology: FeatureOntology object
        Desired Feature Ontology pb2 object to be opened. Returns
        None if neither fails to load.

    """
    try:
        ontology = parse_pbobject(Path(ontology_file).read_text(), FeatureOntologyPb2)
        if ontology is not None:
            logger.debug("Successfully loaded FeatureOntology spec.")
            return ontology
    except Exception:
        logger.error("Failed to load ontology file" + ontology_file + ".")


def generate_uid_from_pbobject(pb_object):
    """Given a pb object, return the deterministic SHA1 hash hexdigest.
    Used for creating unique IDs.

    Parameters
    ----------
    pb_object: object
        A protobuf pb2 object to be hashed.

    Returns
    -------
    Hexdigest of annotation content

    """
    json_string = json.dumps(
        MessageToDict(
            pb_object,
            including_default_value_fields=True,
            preserving_proto_field_name=True,
        ),
        indent=2,
        sort_keys=True,
    )
    out = StringIO()
    out.write(json_string)
    uid = hashlib.sha1(out.getvalue().encode("utf-8")).hexdigest()
    out.close()
    return uid
