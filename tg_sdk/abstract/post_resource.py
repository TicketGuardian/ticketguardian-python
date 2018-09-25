import json
import requests

from .api_resource import APIResource
from .error_handling import raise_response_error


class PostResourceMixin(APIResource):
    @classmethod
    def create(cls, *ext, **params):
        """
        Post a new resource with the given parameters.
            Keyword Arguments:
                instance: An instance of the class making the retrieval.
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
        instance = params.pop('instance', cls())
        url = instance.make_url(*ext)

        response = requests.post(
            url,
            headers=instance.default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            raise_response_error(response)

        if params.pop('raw_data', False):
            return data
        else:
            return instance.construct(**data)
