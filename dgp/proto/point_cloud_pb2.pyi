"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2019-2021 Toyota Research Institute.  All rights reserved.
Definitions for point cloud and point cloud metadata.
"""

import builtins
import collections.abc
import dgp.proto.geometry_pb2
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

@typing.final
class PointCloud(google.protobuf.message.Message):
    """Basic point cloud container for DGP"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ChannelType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ChannelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PointCloud._ChannelType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        X: PointCloud._ChannelType.ValueType  # 0
        """X, Y, and Z coordinates of point."""
        Y: PointCloud._ChannelType.ValueType  # 1
        Z: PointCloud._ChannelType.ValueType  # 2
        INTENSITY: PointCloud._ChannelType.ValueType  # 3
        """Intensity of return at point."""
        R: PointCloud._ChannelType.ValueType  # 4
        """RGB for color."""
        G: PointCloud._ChannelType.ValueType  # 5
        B: PointCloud._ChannelType.ValueType  # 6
        RING: PointCloud._ChannelType.ValueType  # 7
        """The ring index of this point. This is commonly used for spinning lidar."""
        NORMAL_X: PointCloud._ChannelType.ValueType  # 8
        NORMAL_Y: PointCloud._ChannelType.ValueType  # 9
        NORMAL_Z: PointCloud._ChannelType.ValueType  # 10
        TIMESTAMP: PointCloud._ChannelType.ValueType  # 13
        """Timestamp of this point sample, stored as UTC in microseconds"""

    class ChannelType(_ChannelType, metaclass=_ChannelTypeEnumTypeWrapper):
        """Used to describe the values in the pointcloud.
        The ChannelType refers to the dtypes of the point cloud
        stored under the 'filename' key.
        """

    X: PointCloud.ChannelType.ValueType  # 0
    """X, Y, and Z coordinates of point."""
    Y: PointCloud.ChannelType.ValueType  # 1
    Z: PointCloud.ChannelType.ValueType  # 2
    INTENSITY: PointCloud.ChannelType.ValueType  # 3
    """Intensity of return at point."""
    R: PointCloud.ChannelType.ValueType  # 4
    """RGB for color."""
    G: PointCloud.ChannelType.ValueType  # 5
    B: PointCloud.ChannelType.ValueType  # 6
    RING: PointCloud.ChannelType.ValueType  # 7
    """The ring index of this point. This is commonly used for spinning lidar."""
    NORMAL_X: PointCloud.ChannelType.ValueType  # 8
    NORMAL_Y: PointCloud.ChannelType.ValueType  # 9
    NORMAL_Z: PointCloud.ChannelType.ValueType  # 10
    TIMESTAMP: PointCloud.ChannelType.ValueType  # 13
    """Timestamp of this point sample, stored as UTC in microseconds"""

    @typing.final
    class AnnotationsEntry(google.protobuf.message.Message):
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
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> google.protobuf.any_pb2.Any: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: google.protobuf.any_pb2.Any | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FILENAME_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    POINT_FORMAT_FIELD_NUMBER: builtins.int
    POINT_FIELDS_FIELD_NUMBER: builtins.int
    POSE_FIELD_NUMBER: builtins.int
    filename: builtins.str
    """Relative file path for the point cloud
    Supported point cloud formats: compressed numpy (npz) format, polygon file format (ply).
    """
    @property
    def annotations(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.str]:
        """PointCloud annotations
        Maps dgp.proto.AnnotationType (segmentation, instances) to the filename
        containing the point cloud annotation.

        Point cloud annotation schemas are defined in 'annotations.proto'.
        """

    @property
    def metadata(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, google.protobuf.any_pb2.Any]:
        """Optional metadata (i.e. miscellaneous enriched annotations)
        TODO: Support only specific metadata types
        """

    @property
    def point_format(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___PointCloud.ChannelType.ValueType]:
        """Structure of values in the pointcloud file. Each entry in this array specifies
        the field meaning. A simple pointcloud may simply contain X, Y, and Z channels.
        This would mean that the numpy data representation of this would be an
        [N, 3] shape structured array.
        """

    @property
    def point_fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Alternatively, use point fields instead of strongly-typed ChannelType
        For example, radar data can be represented as D-dimensional tensors/matrices with
        point_fields describing the columns for the point cloud data
        """

    @property
    def pose(self) -> dgp.proto.geometry_pb2.Pose:
        """Ego-pose of this datum with respect to the first sample in the scene."""

    def __init__(
        self,
        *,
        filename: builtins.str = ...,
        annotations: collections.abc.Mapping[builtins.int, builtins.str] | None = ...,
        metadata: collections.abc.Mapping[builtins.str, google.protobuf.any_pb2.Any] | None = ...,
        point_format: collections.abc.Iterable[global___PointCloud.ChannelType.ValueType] | None = ...,
        point_fields: collections.abc.Iterable[builtins.str] | None = ...,
        pose: dgp.proto.geometry_pb2.Pose | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pose", b"pose"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["annotations", b"annotations", "filename", b"filename", "metadata", b"metadata", "point_fields", b"point_fields", "point_format", b"point_format", "pose", b"pose"]) -> None: ...

global___PointCloud = PointCloud
