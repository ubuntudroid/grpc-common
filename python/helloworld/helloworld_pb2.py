# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='',
  serialized_pb=_b('\n\x10helloworld.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t23\n\x07Greeter\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=48,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)


import abc
from grpc._adapter import fore
from grpc._adapter import rear
from grpc.framework.assembly import implementations
from grpc.framework.assembly import utilities
class EarlyAdopterGreeterServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def SayHello(self, request):
    raise NotImplementedError()
class EarlyAdopterGreeterServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterGreeterStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def SayHello(self, request):
    raise NotImplementedError()
  SayHello.async = None
def early_adopter_create_Greeter_server(servicer, port, root_certificates, key_chain_pairs):
  method_implementations = {
    "SayHello": utilities.unary_unary_inline(servicer.SayHello),
  }
  import helloworld_pb2
  request_deserializers = {
    "SayHello": helloworld_pb2.HelloRequest.FromString,
  }
  response_serializers = {
    "SayHello": lambda x: x.SerializeToString(),
  }
  link = fore.activated_fore_link(port, request_deserializers, response_serializers, root_certificates, key_chain_pairs)
  return implementations.assemble_service(method_implementations, link)
def early_adopter_create_Greeter_stub(host, port):
  method_implementations = {
    "SayHello": utilities.unary_unary_inline(None),
  }
  import helloworld_pb2
  response_deserializers = {
    "SayHello": helloworld_pb2.HelloReply.FromString,
  }
  request_serializers = {
    "SayHello": lambda x: x.SerializeToString(),
  }
  link = rear.activated_rear_link(host, port, request_serializers, response_deserializers)
  return implementations.assemble_dynamic_inline_stub(method_implementations, link)
# @@protoc_insertion_point(module_scope)