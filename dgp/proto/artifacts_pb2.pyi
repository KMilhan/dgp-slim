"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2019-2021 Toyota Research Institute.  All rights reserved.
Definitions for metadata related to whole datasets and its instances and
splits.
"""

import builtins
import collections.abc
import dgp.proto.dataset_pb2
import dgp.proto.remote_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DatasetArtifacts(google.protobuf.message.Message):
    """Artifacts for a dataset registered in the TRI-ML DGP format."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    ARTIFACT_FIELD_NUMBER: builtins.int
    DERIVED_FROM_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> dgp.proto.dataset_pb2.DatasetMetadata:
        """Dataset-specific metadata
        Note: The metadata in the dataset artifact is
        maintained for traceability purposes.
        """

    @property
    def artifact(self) -> dgp.proto.remote_pb2.RemoteArtifact:
        """DGP-compliant dataset artifact"""

    @property
    def derived_from(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """sha1sum of all parent DatasetArtifacts JSON files this DatasetArtifacts is derived from.
        We are implicitly creating a linked list of DatasetArtifacts where the first item in the
        list has `derived_from` field empty and all subsequent items have it populated.
        """

    def __init__(
        self,
        *,
        metadata: dgp.proto.dataset_pb2.DatasetMetadata | None = ...,
        artifact: dgp.proto.remote_pb2.RemoteArtifact | None = ...,
        derived_from: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["artifact", b"artifact", "metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["artifact", b"artifact", "derived_from", b"derived_from", "metadata", b"metadata"]) -> None: ...

global___DatasetArtifacts = DatasetArtifacts