# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dgp/proto/dataset.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from dgp.proto import remote_pb2 as dgp_dot_proto_dot_remote__pb2
from dgp.proto import scene_pb2 as dgp_dot_proto_dot_scene__pb2
from dgp.proto import statistics_pb2 as dgp_dot_proto_dot_statistics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x64gp/proto/dataset.proto\x12\tdgp.proto\x1a\x19google/protobuf/any.proto\x1a\x16\x64gp/proto/remote.proto\x1a\x15\x64gp/proto/scene.proto\x1a\x1a\x64gp/proto/statistics.proto\"\xec\x05\n\x08Ontology\x12\x35\n\nname_to_id\x18\x01 \x03(\x0b\x32!.dgp.proto.Ontology.NameToIdEntry\x12\x35\n\nid_to_name\x18\x02 \x03(\x0b\x32!.dgp.proto.Ontology.IdToNameEntry\x12\x33\n\x08\x63olormap\x18\x03 \x03(\x0b\x32!.dgp.proto.Ontology.ColormapEntry\x12\x31\n\x07isthing\x18\x04 \x03(\x0b\x32 .dgp.proto.Ontology.IsthingEntry\x12=\n\rsupercategory\x18\x05 \x03(\x0b\x32&.dgp.proto.Ontology.SupercategoryEntry\x12\x42\n\x10segmentation_ids\x18\x06 \x03(\x0b\x32(.dgp.proto.Ontology.SegmentationIdsEntry\x12\x11\n\tignore_id\x18\x07 \x01(\x03\x1a/\n\rNameToIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a/\n\rIdToNameEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a(\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x01(\x05\x12\t\n\x01g\x18\x02 \x01(\x05\x12\t\n\x01\x62\x18\x03 \x01(\x05\x1aJ\n\rColormapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.dgp.proto.Ontology.Color:\x02\x38\x01\x1a.\n\x0cIsthingEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x34\n\x12SupercategoryEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14SegmentationIdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\xbf\x03\n\x0f\x44\x61tasetMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x15\n\rcreation_date\x18\x03 \x01(\t\x12\x0f\n\x07\x63reator\x18\x04 \x01(\t\x12*\n\x0b\x62ucket_path\x18\x05 \x01(\x0b\x32\x15.dgp.proto.RemotePath\x12\'\n\x08raw_path\x18\x06 \x01(\x0b\x32\x15.dgp.proto.RemotePath\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x38\n\x06origin\x18\x08 \x01(\x0e\x32(.dgp.proto.DatasetMetadata.DatasetOrigin\x12\"\n\x1a\x61vailable_annotation_types\x18\t \x03(\x05\x12\x30\n\nstatistics\x18\n \x01(\x0b\x32\x1c.dgp.proto.DatasetStatistics\x12\x18\n\x10\x66rame_per_second\x18\x0b \x01(\x02\x12&\n\x08metadata\x18\x0c \x01(\x0b\x32\x14.google.protobuf.Any\")\n\rDatasetOrigin\x12\n\n\x06PUBLIC\x10\x00\x12\x0c\n\x08INTERNAL\x10\x01\"\xc7\x01\n\x0cSceneDataset\x12,\n\x08metadata\x18\x01 \x01(\x0b\x32\x1a.dgp.proto.DatasetMetadata\x12>\n\x0cscene_splits\x18\x02 \x03(\x0b\x32(.dgp.proto.SceneDataset.SceneSplitsEntry\x1aI\n\x10SceneSplitsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.dgp.proto.SceneFiles:\x02\x38\x01\"\xbe\x01\n\x06\x41gents\x12,\n\x08metadata\x18\x01 \x01(\x0b\x32\x1a.dgp.proto.DatasetMetadata\x12:\n\ragents_splits\x18\x02 \x03(\x0b\x32#.dgp.proto.Agents.AgentsSplitsEntry\x1aJ\n\x11\x41gentsSplitsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.dgp.proto.AgentFiles:\x02\x38\x01\"\x1f\n\nAgentFiles\x12\x11\n\tfilenames\x18\x01 \x03(\t*?\n\x0c\x44\x61tasetSplit\x12\t\n\x05TRAIN\x10\x00\x12\x07\n\x03VAL\x10\x01\x12\x08\n\x04TEST\x10\x02\x12\x11\n\rTRAIN_OVERFIT\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dgp.proto.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ONTOLOGY_NAMETOIDENTRY']._loaded_options = None
  _globals['_ONTOLOGY_NAMETOIDENTRY']._serialized_options = b'8\001'
  _globals['_ONTOLOGY_IDTONAMEENTRY']._loaded_options = None
  _globals['_ONTOLOGY_IDTONAMEENTRY']._serialized_options = b'8\001'
  _globals['_ONTOLOGY_COLORMAPENTRY']._loaded_options = None
  _globals['_ONTOLOGY_COLORMAPENTRY']._serialized_options = b'8\001'
  _globals['_ONTOLOGY_ISTHINGENTRY']._loaded_options = None
  _globals['_ONTOLOGY_ISTHINGENTRY']._serialized_options = b'8\001'
  _globals['_ONTOLOGY_SUPERCATEGORYENTRY']._loaded_options = None
  _globals['_ONTOLOGY_SUPERCATEGORYENTRY']._serialized_options = b'8\001'
  _globals['_ONTOLOGY_SEGMENTATIONIDSENTRY']._loaded_options = None
  _globals['_ONTOLOGY_SEGMENTATIONIDSENTRY']._serialized_options = b'8\001'
  _globals['_SCENEDATASET_SCENESPLITSENTRY']._loaded_options = None
  _globals['_SCENEDATASET_SCENESPLITSENTRY']._serialized_options = b'8\001'
  _globals['_AGENTS_AGENTSSPLITSENTRY']._loaded_options = None
  _globals['_AGENTS_AGENTSSPLITSENTRY']._serialized_options = b'8\001'
  _globals['_DATASETSPLIT']._serialized_start=1769
  _globals['_DATASETSPLIT']._serialized_end=1832
  _globals['_ONTOLOGY']._serialized_start=141
  _globals['_ONTOLOGY']._serialized_end=889
  _globals['_ONTOLOGY_NAMETOIDENTRY']._serialized_start=517
  _globals['_ONTOLOGY_NAMETOIDENTRY']._serialized_end=564
  _globals['_ONTOLOGY_IDTONAMEENTRY']._serialized_start=566
  _globals['_ONTOLOGY_IDTONAMEENTRY']._serialized_end=613
  _globals['_ONTOLOGY_COLOR']._serialized_start=615
  _globals['_ONTOLOGY_COLOR']._serialized_end=655
  _globals['_ONTOLOGY_COLORMAPENTRY']._serialized_start=657
  _globals['_ONTOLOGY_COLORMAPENTRY']._serialized_end=731
  _globals['_ONTOLOGY_ISTHINGENTRY']._serialized_start=733
  _globals['_ONTOLOGY_ISTHINGENTRY']._serialized_end=779
  _globals['_ONTOLOGY_SUPERCATEGORYENTRY']._serialized_start=781
  _globals['_ONTOLOGY_SUPERCATEGORYENTRY']._serialized_end=833
  _globals['_ONTOLOGY_SEGMENTATIONIDSENTRY']._serialized_start=835
  _globals['_ONTOLOGY_SEGMENTATIONIDSENTRY']._serialized_end=889
  _globals['_DATASETMETADATA']._serialized_start=892
  _globals['_DATASETMETADATA']._serialized_end=1339
  _globals['_DATASETMETADATA_DATASETORIGIN']._serialized_start=1298
  _globals['_DATASETMETADATA_DATASETORIGIN']._serialized_end=1339
  _globals['_SCENEDATASET']._serialized_start=1342
  _globals['_SCENEDATASET']._serialized_end=1541
  _globals['_SCENEDATASET_SCENESPLITSENTRY']._serialized_start=1468
  _globals['_SCENEDATASET_SCENESPLITSENTRY']._serialized_end=1541
  _globals['_AGENTS']._serialized_start=1544
  _globals['_AGENTS']._serialized_end=1734
  _globals['_AGENTS_AGENTSSPLITSENTRY']._serialized_start=1660
  _globals['_AGENTS_AGENTSSPLITSENTRY']._serialized_end=1734
  _globals['_AGENTFILES']._serialized_start=1736
  _globals['_AGENTFILES']._serialized_end=1767
# @@protoc_insertion_point(module_scope)
