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

import pandas as pd
import logging
from typing import Optional
from witness.core.abstract import AbstractLoader, AbstractSerializer, AbstractExtractor

log = logging.getLogger(__name__)


class PandasSerializer(AbstractSerializer):

    def to_batch(self, raw, *args, **kwargs):
        data = raw.to_dict(orient='records')
        return data

    def from_batch(self, data, *args, dtype='str', **kwargs):
        df = pd.DataFrame(data, dtype=dtype)
        return df


class PandasLoader(AbstractLoader):

    def __init__(self, uri, serializer: Optional[AbstractSerializer] = PandasSerializer()):
        super().__init__(uri)
        self.serializer = serializer

    def prepare(self, batch):
        super().prepare(batch)
        df = self.serializer.from_batch(batch.data)
        self.output = df
        return self

    def attach_meta(self, meta_elements: Optional[list[str]] = None):
        super().attach_meta(meta_elements)
        for element in self.meta_to_attach:
            self.output[element] = self.meta_to_attach[element]

        return self

    def load(self):
        raise NotImplementedError


class PandasExtractor(AbstractExtractor):
    """
    Basic pandas extractor class.
    Provides a single 'unify' method for all child pandas extractors.
    """
    def __init__(self, uri):
        super().__init__(uri)
        self.serializer = PandasSerializer()

    output: pd.DataFrame

    def extract(self):
        self._set_extraction_timestamp()

    def unify(self):

        data = self.serializer.to_batch(self.output)
        meta = {'extraction_timestamp': self.extraction_timestamp,
                'record_source': self.uri}

        setattr(self, 'output', {'meta': meta, 'data': data})

        return self
