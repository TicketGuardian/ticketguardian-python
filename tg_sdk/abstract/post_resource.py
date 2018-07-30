import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class PostResourceMixin(APIResource):
    @classmethod
    def post(cls, **params):
        """
        Post a new resource with the given parameters.

            Returns:
                An instance of the object that was just posted.
                If a bad request is made then an empty resource object is
                returned.
        """
        instance = cls()
        url = "{}/api/v2/{}/".format(
            instance.core_url,
            instance.resource
        )

        response = requests.post(
            url,
            headers=instance.default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            # TODO(Justin): ADD ERROR HANDLING
            data = {}

        return instance.construct(**data)
