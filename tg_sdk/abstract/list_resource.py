import json
import requests

from tg_sdk.abstract.api_resource import APIResource
from tg_sdk.abstract.error_handling import raise_response_error
from tg_sdk.abstract.resource_list import Resource_List


class ListResourceMixin(APIResource):

    @classmethod
    def list(cls, limit=None, *ext, **params):
        """
        Returns a list of resources that will lazy load objects
        """
        return Resource_List(cls=cls, size=limit)

    def get_list(self, *ext, **params):
        """
        Retrieve multiple resources and return a list of instances of child
        objects initialized with the data received. Any additional filters can
        be added into params as a keyword arg.

            Keyword Arguments:
                obj_list = The list of objects to be updated.
                offset: The starting index of where the list will be updated.
                limit: The maximum resources that will be returned.
                raw_data: A boolean value that will tell this method to return
                          the raw list data.

            Optional Arguments:
                *ext: Strings that are extensions of the url
                    This should only be used from within resource methods.


            Returns:
                list of objects: A list of instances of the child object that
                called. If an error occurs or a bad request is made then an
                empty list is returned.
                -or-
                list of raw data: If raw_data is true.
        """
        resources = []
        raw_data = params.pop('raw_data', False)
        limit = params.pop("limit", None)
        url = self._make_url(*ext)

        response = requests.request(
            "GET",
            url,
            headers=self._default_headers,
            params=params
        )
        if response.ok:
            data = json.loads(response.text)
            if raw_data:
                return data
            else:
                resources += [
                    self._construct(**res)
                    for res in data.get('results', [])
                ]
        else:
            raise_response_error(response)

        return resources[:limit]

    def get_resource_count(self):
        data = self.get_list(obj_list=[], raw_data=True, limit=1)
        return data.get("count")
