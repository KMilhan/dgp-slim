"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2019-2021 Toyota Research Institute.  All rights reserved.
Definitions for metadata related to whole datasets and its instances and
splits.
"""

import builtins
import collections.abc
import dgp.proto.remote_pb2
import dgp.proto.scene_pb2
import dgp.proto.statistics_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DatasetSplit:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DatasetSplitEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DatasetSplit.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TRAIN: _DatasetSplit.ValueType  # 0
    VAL: _DatasetSplit.ValueType  # 1
    TEST: _DatasetSplit.ValueType  # 2
    TRAIN_OVERFIT: _DatasetSplit.ValueType  # 3

class DatasetSplit(_DatasetSplit, metaclass=_DatasetSplitEnumTypeWrapper):
    """Dataset Split Enum"""

TRAIN: DatasetSplit.ValueType  # 0
VAL: DatasetSplit.ValueType  # 1
TEST: DatasetSplit.ValueType  # 2
TRAIN_OVERFIT: DatasetSplit.ValueType  # 3
global___DatasetSplit = DatasetSplit

@typing.final
class Ontology(google.protobuf.message.Message):
    """Dataset ontology"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class NameToIdEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class IdToNameEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class Color(google.protobuf.message.Message):
        """Various look-up tables"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        R_FIELD_NUMBER: builtins.int
        G_FIELD_NUMBER: builtins.int
        B_FIELD_NUMBER: builtins.int
        r: builtins.int
        g: builtins.int
        b: builtins.int
        def __init__(
            self,
            *,
            r: builtins.int = ...,
            g: builtins.int = ...,
            b: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["b", b"b", "g", b"g", "r", b"r"]) -> None: ...

    @typing.final
    class ColormapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___Ontology.Color: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___Ontology.Color | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class IsthingEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.bool
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class SupercategoryEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class SegmentationIdsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_TO_ID_FIELD_NUMBER: builtins.int
    ID_TO_NAME_FIELD_NUMBER: builtins.int
    COLORMAP_FIELD_NUMBER: builtins.int
    ISTHING_FIELD_NUMBER: builtins.int
    SUPERCATEGORY_FIELD_NUMBER: builtins.int
    SEGMENTATION_IDS_FIELD_NUMBER: builtins.int
    IGNORE_ID_FIELD_NUMBER: builtins.int
    ignore_id: builtins.int
    @property
    def name_to_id(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.int]:
        """Dictionary maintaining the class name to unique class id mapping"""

    @property
    def id_to_name(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.str]:
        """Inverted mapping of name_to_id"""

    @property
    def colormap(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___Ontology.Color]: ...
    @property
    def isthing(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.bool]: ...
    @property
    def supercategory(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.str]: ...
    @property
    def segmentation_ids(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.int]: ...
    def __init__(
        self,
        *,
        name_to_id: collections.abc.Mapping[builtins.str, builtins.int] | None = ...,
        id_to_name: collections.abc.Mapping[builtins.int, builtins.str] | None = ...,
        colormap: collections.abc.Mapping[builtins.int, global___Ontology.Color] | None = ...,
        isthing: collections.abc.Mapping[builtins.int, builtins.bool] | None = ...,
        supercategory: collections.abc.Mapping[builtins.int, builtins.str] | None = ...,
        segmentation_ids: collections.abc.Mapping[builtins.int, builtins.int] | None = ...,
        ignore_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["colormap", b"colormap", "id_to_name", b"id_to_name", "ignore_id", b"ignore_id", "isthing", b"isthing", "name_to_id", b"name_to_id", "segmentation_ids", b"segmentation_ids", "supercategory", b"supercategory"]) -> None: ...

global___Ontology = Ontology

@typing.final
class DatasetMetadata(google.protobuf.message.Message):
    """Dataset metadata specific to a particular SceneDataset."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _DatasetOrigin:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _DatasetOriginEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DatasetMetadata._DatasetOrigin.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PUBLIC: DatasetMetadata._DatasetOrigin.ValueType  # 0
        INTERNAL: DatasetMetadata._DatasetOrigin.ValueType  # 1

    class DatasetOrigin(_DatasetOrigin, metaclass=_DatasetOriginEnumTypeWrapper):
        """Dataset origin identifier (i.e. whether the dataset originated
        internally or from the public domain)
        """

    PUBLIC: DatasetMetadata.DatasetOrigin.ValueType  # 0
    INTERNAL: DatasetMetadata.DatasetOrigin.ValueType  # 1

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    CREATION_DATE_FIELD_NUMBER: builtins.int
    CREATOR_FIELD_NUMBER: builtins.int
    BUCKET_PATH_FIELD_NUMBER: builtins.int
    RAW_PATH_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ORIGIN_FIELD_NUMBER: builtins.int
    AVAILABLE_ANNOTATION_TYPES_FIELD_NUMBER: builtins.int
    STATISTICS_FIELD_NUMBER: builtins.int
    FRAME_PER_SECOND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Dataset name"""
    version: builtins.str
    """Dataset semantic version
    TODO: Establish semantic versioning.
    """
    creation_date: builtins.str
    """Date of dataset creation: yyyy-mm-dd
    TODO: Change this to datetime
    """
    creator: builtins.str
    """Dataset creator
    (for e.g., unique email address: john.doe@domain.com)
    """
    description: builtins.str
    """Short description of the dataset (~200 characters)"""
    origin: global___DatasetMetadata.DatasetOrigin.ValueType
    frame_per_second: builtins.float
    """(Optional) Sampling rate of the dataset
    This is used to synchronize different fps from different datasets.
    """
    @property
    def bucket_path(self) -> dgp.proto.remote_pb2.RemotePath:
        """Remote path to DGP-compliant dataset (s3://<bucket>/)"""

    @property
    def raw_path(self) -> dgp.proto.remote_pb2.RemotePath:
        """Remote path to the raw dataset (s3://<bucket>/bdd100k/)"""

    @property
    def available_annotation_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """List of annotation types supported by the dataset
        See dgp.proto.AnnotationType in dgp/proto/annotations.proto
        """

    @property
    def statistics(self) -> dgp.proto.statistics_pb2.DatasetStatistics:
        """(Optional) Dataset-specific statistics
        This is usually of the TRAIN set.
        """

    @property
    def metadata(self) -> google.protobuf.any_pb2.Any:
        """Container for generic metadata.
        Metadata of "Any" type is useful in cases where the metadata type is
        specific to a paricular dataset type. For example, this field can contain:
        - a bare string which contains structured data like json, yaml, etc.
        - dataset specific metadata with some proto definition (assuming the
          compiled proto is available to both the writer and reader of the dataset.
        """

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        version: builtins.str = ...,
        creation_date: builtins.str = ...,
        creator: builtins.str = ...,
        bucket_path: dgp.proto.remote_pb2.RemotePath | None = ...,
        raw_path: dgp.proto.remote_pb2.RemotePath | None = ...,
        description: builtins.str = ...,
        origin: global___DatasetMetadata.DatasetOrigin.ValueType = ...,
        available_annotation_types: collections.abc.Iterable[builtins.int] | None = ...,
        statistics: dgp.proto.statistics_pb2.DatasetStatistics | None = ...,
        frame_per_second: builtins.float = ...,
        metadata: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["bucket_path", b"bucket_path", "metadata", b"metadata", "raw_path", b"raw_path", "statistics", b"statistics"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["available_annotation_types", b"available_annotation_types", "bucket_path", b"bucket_path", "creation_date", b"creation_date", "creator", b"creator", "description", b"description", "frame_per_second", b"frame_per_second", "metadata", b"metadata", "name", b"name", "origin", b"origin", "raw_path", b"raw_path", "statistics", b"statistics", "version", b"version"]) -> None: ...

global___DatasetMetadata = DatasetMetadata

@typing.final
class SceneDataset(google.protobuf.message.Message):
    """Scene Dataset

    Scenes are stored in the DGP under the following structure:
     <scene_dataset_name>
     ├── <scene_name>
     │   ├── bounding_box_2d
     │   │   └── ...
     │   ├── bounding_box_3d
     │   │   └── ...
     │   ├── calibration
     │   │   └── <calibration_hash>.json
     │   │   └── ...
     │   ├── ontology
     │   │   └── <ontology_hash>.json
     │   │   └── ...
     │   ├── point_cloud
     │   │   └── ...
     │   ├── rgb
     │   │   └── ...
     │   ├── agent_tracks
     │   │   └── agent_track_<hash>.json
     │   │   └── ...
     │   ├── agents_slices
     │   │   └── agent_slice<hash>.json
     │   │   └── ...
     |   └── ...
     │   └── scene_<scene_hash>.json
     │   └── agent_<agent_hash>.json
     │   └── map_<agent_hash>.json
     └── ...
     └── scene_dataset_v1.0.json
     └── agents_v1.0.json
     └── map_elements_v1.0.json
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class SceneSplitsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> dgp.proto.scene_pb2.SceneFiles: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: dgp.proto.scene_pb2.SceneFiles | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    METADATA_FIELD_NUMBER: builtins.int
    SCENE_SPLITS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> global___DatasetMetadata:
        """Dataset-specific metadata"""

    @property
    def scene_splits(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, dgp.proto.scene_pb2.SceneFiles]:
        """List of scenes recorded for each split (train/val/test) in this dataset.
        Note: This corresponds to a particular task in the dataset.
        Maps <DatasetSplit, Scenes>
        """

    def __init__(
        self,
        *,
        metadata: global___DatasetMetadata | None = ...,
        scene_splits: collections.abc.Mapping[builtins.int, dgp.proto.scene_pb2.SceneFiles] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata", "scene_splits", b"scene_splits"]) -> None: ...

global___SceneDataset = SceneDataset

@typing.final
class Agents(google.protobuf.message.Message):
    """Road actors in the Scene (Pedestrians, vehicles, etc)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class AgentsSplitsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___AgentFiles: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___AgentFiles | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    METADATA_FIELD_NUMBER: builtins.int
    AGENTS_SPLITS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> global___DatasetMetadata:
        """Dataset-specific metadata"""

    @property
    def agents_splits(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___AgentFiles]:
        """List of SceneAgents recorded for each split (train/val/test) in this dataset.
        Note: This corresponds to a particular task in the dataset.
        Maps <DatasetSplit, SceneAgents>
        """

    def __init__(
        self,
        *,
        metadata: global___DatasetMetadata | None = ...,
        agents_splits: collections.abc.Mapping[builtins.int, global___AgentFiles] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["agents_splits", b"agents_splits", "metadata", b"metadata"]) -> None: ...

global___Agents = Agents

@typing.final
class AgentFiles(google.protobuf.message.Message):
    """A collection of agent files."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILENAMES_FIELD_NUMBER: builtins.int
    @property
    def filenames(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Relative file paths for the json files serialized from AgentGroup message.

        An AgentGroup message is serialized and stored under the following naming convention:
           <scene_dir>/agents_<scene_hash>.json
        where <agents_hash> is the deterministic deterministic SHA1 hash hexdigest of a agentgroup and
        served as the version of the scene, see dgp.utils.protobuf.generate_uid_from_pbobject
        for details.
        """

    def __init__(
        self,
        *,
        filenames: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filenames", b"filenames"]) -> None: ...

global___AgentFiles = AgentFiles