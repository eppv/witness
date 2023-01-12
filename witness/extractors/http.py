
from witness.core.abstract import AbstractExtractor, AbstractSerializer
from witness.serializers.http import JsonSerializer
import requests
from requests.auth import AuthBase
from typing import Optional


class HttpGetExtractor(AbstractExtractor):

    def __init__(self,
                 uri,
                 params: Optional[dict] = None,
                 auth: Optional[AuthBase] = None,
                 serializer: Optional[AbstractSerializer] = JsonSerializer()):
        self.serializer = serializer
        self.params: dict or None = params
        self.auth = auth
        super().__init__(uri)

    def extract(self):

        response = requests.get(url=self.uri, params=self.params, auth=self.auth)
        response.raise_for_status()

        setattr(self, 'output', response)
        self._set_extraction_timestamp()

        return self

    def unify(self):
        meta = {'extraction_timestamp': self.extraction_timestamp,
                'record_source': self.uri}
        data = self.serializer.to_batch(self.output)
        setattr(self, 'output', {'meta': meta, 'data': data})
        return self
