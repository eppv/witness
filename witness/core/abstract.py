
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

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from datetime import datetime


class AbstractBatch(metaclass=ABCMeta):

    @abstractmethod
    def fill(self, extractor):
        raise NotImplemented

    @abstractmethod
    def push(self, loader):
        raise NotImplemented


class AbstractExtractor(metaclass=ABCMeta):

    def __init__(self, uri=None):

        self.uri = uri
        self.output = None
        self.extraction_timestamp: datetime | None = None

    @abstractmethod
    def _set_extraction_timestamp(self):
        raise NotImplementedError

    @abstractmethod
    def extract(self):
        raise NotImplementedError

    @abstractmethod
    def unify(self):
        raise NotImplementedError


class AbstractLoader(metaclass=ABCMeta):

    def __init__(self, uri=None):

        self.uri = uri
        self.output = None

    @abstractmethod
    def prepare(self, batch):
        raise NotImplementedError

    @abstractmethod
    def load(self):
        raise NotImplementedError
