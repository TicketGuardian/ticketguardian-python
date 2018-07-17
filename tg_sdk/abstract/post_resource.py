import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class PostResourceMixin(APIResource):

    def post(self, **params):
        """
        Post a new resource with the given parameters.

            Returns:
                An instance of the object that was just posted.
                If a bad request is made then an empty resource object is
                returned.
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
            data = {}

        instance = self.new_instance(**self.credentials)
        return instance.construct(data)
