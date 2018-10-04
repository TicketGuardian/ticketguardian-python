import json
import requests

from tg_sdk.abstract.api_resource import APIResource
from tg_sdk.abstract.error_handling import raise_response_error


class ListResourceMixin(APIResource):
    @classmethod
    def list(cls, *ext, **params):
        """
        Retrieve multiple resources and return a list of instances of child
        objects initialized with the data received. Any additional filters can
        be added into params as a keyword arg.

            Keyword Arguments:
                instance (object): An instance of the class making
                                   the retrieval.
                ext: Strings that are extensions of the url
                     This should only be used from within resource methods.
                limit: The maximum resources that will be returned.
                raw_data: A boolean value that will tell this method to return
                          the raw list data.

            Returns:
                list of objects: A list of instances of the child object that
                called. If an error occurs or a bad request is made then an
                empty list is returned.
                -or-
                list of raw data: If raw_data is true.
        """
        instance = params.pop('instance', cls())
        resources = []
        raw_data = params.pop('raw_data', False)
        limit = params.get("limit", None)
        url = instance._make_url(*ext)

        while url and (limit is None or limit > len(resources)):
            response = requests.request(
                "GET",
                url,
                headers=instance._default_headers,
                params=params
            )
            if response.ok:
                data = json.loads(response.text)
                if raw_data:
                    new = [res for res in data.get('results', [])]
                else:
                    new = [
                        instance._construct(**res)
                        for res in data.get('results', [])
                    ]
                resources += new
                url = data.get('next')
            else:
                raise_response_error(response)
        return resources[:limit]
