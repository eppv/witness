#  Copyright (c) 2022.  Eugene Popov.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from witness import Batch, MetaData
from tests import conftest

calibration_meta = conftest.batch_meta
calibration_data = conftest.batch_data


def test_info_full_empty():
    batch = Batch()
    assert batch.info() == "Batch object does not contain any data or meta."
    print(batch.info())


def test_info(fxtr_batch):
    fxtr_batch.info(print_output=True)


def test_auto_creating_meta():
    batch = Batch(calibration_data)
    assert isinstance(batch.meta, MetaData)
