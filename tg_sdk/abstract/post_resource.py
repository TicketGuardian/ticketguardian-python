import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class PostResourceMixin(APIResource):
    @classmethod
    def create(cls, **params):
        """
        Post a new resource with the given parameters.
            Keyword Arguments:
                ext: A list of strings that are extensions of the url
                     This should only be used from within resource methods.
                raw_data: A boolean value that will tell this method to return
                          the raw list data.
            Returns:
                An instance of the object that was just posted.
                If a bad request is made then an empty resource object is
                returned.
                -or-
                dict of raw data: If raw_data is true.
        """
        instance = cls()
        url = instance.make_url(*params.pop('ext', []))

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

        if params.pop('raw_data', False):
            return data
        else:
            return instance.construct(**data)
