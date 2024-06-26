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

import pytest

xfail = pytest.mark.xfail


def test_prepare(fxtr_pandas_loader, fxtr_batch):
    fxtr_pandas_loader.prepare(fxtr_batch)


@xfail
def test_attach_meta_no_batch(fxtr_pandas_loader):
    fxtr_pandas_loader.attach_meta()


def test_attach_meta(fxtr_pandas_loader, fxtr_batch):
    fxtr_pandas_loader.prepare(fxtr_batch).attach_meta()


def test_load(fxtr_pandas_loader, fxtr_batch):
    fxtr_pandas_loader.prepare(fxtr_batch).load()


def test_load_meta_attached(fxtr_pandas_loader, fxtr_batch):
    fxtr_pandas_loader.prepare(fxtr_batch).attach_meta().load()


def test_load_chosen_meta_attached(fxtr_pandas_loader, fxtr_batch):
    fxtr_pandas_loader.prepare(fxtr_batch).attach_meta(["record_source"]).load()


if __name__ == "__main__":
    pytest.main()
