# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/proto/hello.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18protos/proto/hello.proto\x12\x05hello\"\'\n\x13SendGreetingRequest\x12\x10\n\x08greeting\x18\x01 \x01(\t\"(\n\x14SendGreetingResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t2Z\n\x0fServiceGreeting\x12G\n\x0cSendGreeting\x12\x1a.hello.SendGreetingRequest\x1a\x1b.hello.SendGreetingResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.proto.hello_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SENDGREETINGREQUEST']._serialized_start=35
  _globals['_SENDGREETINGREQUEST']._serialized_end=74
  _globals['_SENDGREETINGRESPONSE']._serialized_start=76
  _globals['_SENDGREETINGRESPONSE']._serialized_end=116
  _globals['_SERVICEGREETING']._serialized_start=118
  _globals['_SERVICEGREETING']._serialized_end=208
# @@protoc_insertion_point(module_scope)
