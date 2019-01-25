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
                raw_data (bool): A boolean value that will tell this method to
                                 return the raw list data.
        """
        url = self._make_url(resource_id, *ext)
        raw_data = params.pop('raw_data', False)

        res = requests.patch(
            url,
            headers=self._default_headers,
            json=params
        )
        if not res.ok:
            raise_response_error(res)

        data = res.json()

        return data if raw_data else self
