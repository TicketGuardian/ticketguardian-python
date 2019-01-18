import requests

from ticketguardian.abstract.api_resource import APIResource
from ticketguardian.abstract.error_handling import raise_response_error


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
        raw_data = params.pop('raw_data', False)

        response = requests.put(
            url,
            headers=self._default_headers,
            json=params
        )

        if not response.ok:
            raise_response_error(response)

        data = response.json()

        for key in data:
            setattr(self, key, data[key])

        return data if raw_data else None
