import requests

from ticketguardian.abstract.api_resource import APIResource
from ticketguardian.abstract.error_handling import raise_response_error


class PatchResourceMixin(APIResource):

    def patch(self, resource_id, *args, **kwargs):
        url = self._make_url(resource_id, *args)

        response = requests.patch(
            url,
            headers=self._default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
            return self._construct(**data)
        else:
            raise_response_error(response)
