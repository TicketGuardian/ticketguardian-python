import json
import requests

from tg_sdk.abstract.api_resource import APIResource
from tg_sdk.abstract.error_handling import raise_response_error


class PostResourceMixin(APIResource):
    @classmethod
    def create(cls, *ext, **params):
        """ Post a new resource with the given parameters.
            Keyword Arguments:
                instance: An instance of the class making the retrieval.
                ext: Strings that are extensions of the url
                     This should only be used from within resource methods.
                raw_data (bool): A boolean value that will tell this method to
                                 return the raw list data.
            Returns:
                An instance of the object that was just posted.
                If a bad request is made then an empty resource object is
                returned.
                -or-
                dict of raw data: If raw_data is true.
        """
        instance = params.pop('instance')
        if not instance:
            instance = cls()

        url = instance._make_url(*ext)

        response = requests.post(
            url,
            headers=instance._default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            raise_response_error(response)

        if params.pop('raw_data', False):
            return data
        else:
            return instance._construct(**data)
