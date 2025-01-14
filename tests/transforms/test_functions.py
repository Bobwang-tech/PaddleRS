# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy

import paddlers.transforms as T
from testing_utils import CpuCommonTest
from data import build_input_from_file

__all__ = ['TestMatchHistograms', 'TestMatchByRegression']


class TestMatchHistograms(CpuCommonTest):
    def setUp(self):
        self.inputs = [
            build_input_from_file(
                "data/ssmt/test_mixed_binary.txt", prefix="./data/ssmt")
        ]

    def test_output_shape(self):
        decoder = T.DecodeImg()
        for input in copy.deepcopy(self.inputs):
            for sample in input:
                sample = decoder(sample)
                im_out = T.functions.match_histograms(sample['image'],
                                                      sample['image2'])
                self.check_output_equal(im_out.shape, sample['image2'].shape)
                im_out = T.functions.match_histograms(sample['image2'],
                                                      sample['image'])
                self.check_output_equal(im_out.shape, sample['image'].shape)


class TestMatchByRegression(CpuCommonTest):
    def setUp(self):
        self.inputs = [
            build_input_from_file(
                "data/ssmt/test_mixed_binary.txt", prefix="./data/ssmt")
        ]

    def test_output_shape(self):
        decoder = T.DecodeImg()
        for input in copy.deepcopy(self.inputs):
            for sample in input:
                sample = decoder(sample)
                im_out = T.functions.match_by_regression(sample['image'],
                                                         sample['image2'])
                self.check_output_equal(im_out.shape, sample['image2'].shape)
                im_out = T.functions.match_by_regression(sample['image2'],
                                                         sample['image'])
                self.check_output_equal(im_out.shape, sample['image'].shape)
