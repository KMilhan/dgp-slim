"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2019-2021 Toyota Research Institute.  All rights reserved.
Definitions for OntologyItem and Ontology.
OntologyItem and Ontology are defined in an Object Oriented way for the ease of downstream
consumption. Ontology is simply a collection of multiple OntologyItems that contain all
property fields that represent a category/concept.
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class OntologyItem(google.protobuf.message.Message):
    """An Ontology represents a set of unique concepts/categories that expresses their properties.
    An OntologyItem defines a single, unique element within in an Ontology.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Color(google.protobuf.message.Message):
        """RGB color code to colorize a bounding_box, pixel, mask, etc of this OntologyItem
        in the visualization tool.
        """

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

    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    ISTHING_FIELD_NUMBER: builtins.int
    SUPERCATEGORY_FIELD_NUMBER: builtins.int
    name: builtins.str
    """OntologyItem name. For e.g., 'Vehicle', 'Truck', 'Pedestrian', etc."""
    id: builtins.int
    """OntologyItem id.
    Note: Downstream consumption code ought to assert if every OntologyItem.id is
    unique in an Ontology.
    """
    isthing: builtins.bool
    """True if this OntologyItem is a countable object such as people, car, etc.
    False if this OntologyItem is an amorphous region without instance-level annotation of
    similar texture such as road, sky, etc.
    """
    supercategory: builtins.str
    """Name of the parent OntologyItem."""
    @property
    def color(self) -> global___OntologyItem.Color:
        """OntologyItem RGB color code."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        id: builtins.int = ...,
        color: global___OntologyItem.Color | None = ...,
        isthing: builtins.bool = ...,
        supercategory: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["color", b"color"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["color", b"color", "id", b"id", "isthing", b"isthing", "name", b"name", "supercategory", b"supercategory"]) -> None: ...

global___OntologyItem = OntologyItem

@typing.final
class Ontology(google.protobuf.message.Message):
    """Ontology for dgp.proto.Scene."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OntologyItem]:
        """List of OntologyItems."""

    def __init__(
        self,
        *,
        items: collections.abc.Iterable[global___OntologyItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["items", b"items"]) -> None: ...

global___Ontology = Ontology

@typing.final
class FeatureOntologyItem(google.protobuf.message.Message):
    """A Feature Ontology represents a set of unique feature fields that expresses their properties.
    A FeatureOntologyItem defines a single, unique element within in an FeatureOntology.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    FEATURE_VALUE_TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """OntologyItem name. For e.g., 'Speed', 'Link_to_rasterized_image', 'parking_attribute', etc."""
    id: builtins.int
    """FeatureOntologyItem id.
    Note: Downstream consumption code ought to assert if every FeatureOntologyItem.id is
    unique in an Ontology.
    """
    feature_value_type: builtins.int
    """Specify the feature value type in dgp.proto.features."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        id: builtins.int = ...,
        feature_value_type: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["feature_value_type", b"feature_value_type", "id", b"id", "name", b"name"]) -> None: ...

global___FeatureOntologyItem = FeatureOntologyItem

@typing.final
class FeatureOntology(google.protobuf.message.Message):
    """Feature ontology for dgp.proto.agent."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeatureOntologyItem]:
        """List of FeatureOntologyItems."""

    def __init__(
        self,
        *,
        items: collections.abc.Iterable[global___FeatureOntologyItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["items", b"items"]) -> None: ...

global___FeatureOntology = FeatureOntology