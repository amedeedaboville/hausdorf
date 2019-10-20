# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import smr_pb2 as smr__pb2


class SmrStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Search = channel.unary_unary(
        '/proto.Smr/Search',
        request_serializer=smr__pb2.SearchRequest.SerializeToString,
        response_deserializer=smr__pb2.SearchResponse.FromString,
        )
    self.AddPiece = channel.unary_unary(
        '/proto.Smr/AddPiece',
        request_serializer=smr__pb2.AddPieceRequest.SerializeToString,
        response_deserializer=smr__pb2.AddPieceResponse.FromString,
        )
    self.GetPieceIds = channel.unary_unary(
        '/proto.Smr/GetPieceIds',
        request_serializer=smr__pb2.GetPieceIdsRequest.SerializeToString,
        response_deserializer=smr__pb2.GetPieceIdsResponse.FromString,
        )


class SmrServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Search(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPiece(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPieceIds(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SmrServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=smr__pb2.SearchRequest.FromString,
          response_serializer=smr__pb2.SearchResponse.SerializeToString,
      ),
      'AddPiece': grpc.unary_unary_rpc_method_handler(
          servicer.AddPiece,
          request_deserializer=smr__pb2.AddPieceRequest.FromString,
          response_serializer=smr__pb2.AddPieceResponse.SerializeToString,
      ),
      'GetPieceIds': grpc.unary_unary_rpc_method_handler(
          servicer.GetPieceIds,
          request_deserializer=smr__pb2.GetPieceIdsRequest.FromString,
          response_serializer=smr__pb2.GetPieceIdsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Smr', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
