import requests
import json

from tg_sdk.abstract.api_resource import APIResource


class PostResourceMixin(APIResource):

    def post(self, **params):
        """
        Post a new resource with the given parameters.

            Returns:
                An instance of the object that was just posted.
        """
        url = "{}/api/v2/{}/".format(
            self.core_url,
            self.resource
        )

        response = requests.post(
            url,
            headers=self.default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            # TODO(Justin): ADD ERROR HANDLING
            return
        instance = self.new_instance(**self.credentials)
        return instance.construct(data)
