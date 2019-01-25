import requests

from ticketguardian.abstract.api_resource import APIResource
from ticketguardian.abstract.error_handling import raise_response_error


class PatchResourceMixin(APIResource):

    def patch(self, request, *args, **kwargs):
        """
        Patch a resource with kwargs.
            Keyword Arguments:
                ext: Strings that are extensions of the url
                     This should only be used from within resource methods.
        """
        url = self._make_url(resource_id, *ext)

        res = requests.patch(
            url,
            headers=self._default_headers,
            json=params
        )
        if not res.ok:
            raise_response_error(res)

        data = res.json()

        return data
