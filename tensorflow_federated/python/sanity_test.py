# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for sanity."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

from tensorflow.core.framework import tensor_shape_pb2
from tensorflow.core.framework import types_pb2

from tensorflow_federated.proto.v0 import computation_pb2 as pb


class SanityTest(unittest.TestCase):

  def test_sanity(self):
    c = pb.Computation(type=pb.FunctionType(parameter=pb.Type(
        tuple=pb.NamedTupleType(element=[pb.NamedTupleType.Element(
            name='foo', value=pb.Type(tensor=pb.TensorType(
                dtype=types_pb2.DT_FLOAT,
                shape=tensor_shape_pb2.TensorShapeProto(
                    dim=[tensor_shape_pb2.TensorShapeProto.Dim(size=5)]))))]))))
    self.assertEqual(
        c.type.parameter.tuple.element[0].name, 'foo')
    self.assertEqual(
        c.type.parameter.tuple.element[0].value.tensor.shape.dim[0].size, 5)


if __name__ == '__main__':
  unittest.main()
