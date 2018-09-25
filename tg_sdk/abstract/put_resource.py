import json
import requests

from .api_resource import APIResource
from .error_handling import raise_response_error


class PutResourceMixin(APIResource):
    def update(self, *ext, **params):
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
        url = self.make_url(*ext, default=[self.id])

        response = requests.put(
            url,
            headers=self.default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
            for key in data:
                setattr(self, '_' + key, data[key])
        else:
            raise_response_error(response)
