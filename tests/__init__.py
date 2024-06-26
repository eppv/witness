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

from os import path, getcwd
import pytest

# pytest decorators shortcuts
xfail = pytest.mark.xfail
parametrize = pytest.mark.parametrize

# mock resources shortcuts

proj_dir_uri = './'
proj_dir_path = path.abspath(proj_dir_uri)

while "tests" in proj_dir_path:
    proj_dir_uri = '../' + proj_dir_uri
    proj_dir_path = path.abspath(proj_dir_uri)


temp_dir = path.abspath(f"{proj_dir_uri}/temp")
files_dir = path.abspath(f"{proj_dir_uri}/temp/files")
