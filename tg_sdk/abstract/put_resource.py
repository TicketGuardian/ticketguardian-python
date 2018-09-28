import json
import requests

from tg_sdk.abstract.api_resource import APIResource
from tg_sdk.abstract.error_handling import raise_response_error


class PutResourceMixin(APIResource):
    def update(self, resource_id, *ext, **params):
        """
        Update a currently existing resource.
            Keyword Arguments:
                ext: An extension of the url if extra args are needed.
                     Does not need the leading or trailing '/'.

            Returns:
                An instance of the object that is being updated.
                If a bad request is made then an empty instance of the resource
                object is returned.
        """
        url = self._make_url(resource_id, *ext)

        response = requests.put(
            url,
            headers=self._default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
            for key in data:
                setattr(self, key, data[key])
        else:
            raise_response_error(response)
