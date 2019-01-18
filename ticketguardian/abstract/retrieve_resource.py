import json
import requests

from ticketguardian.abstract.api_resource import APIResource
from ticketguardian.abstract.error_handling import raise_response_error


class RetrieveResourceMixin(APIResource):
    def __getattr__(self, attr):
        if not self.is_updated:
            self.is_updated = True
            self._get_missing_attrs()
            return getattr(self, attr)
        raise AttributeError

    @classmethod
    def retrieve(cls, resource_id, *ext, **params):
        """
        Retrieve a single resource and initialize an instance of the child
        object that called.

            Arguments:
                resource_id: The unique id of the resource.

            Keyword Arguments:
                instance (object): An instance of the class making the
                                   retrieval.
                ext: Strings that are extensions of the url
                     This should only be used from within resource methods.
                raw_data (bool): A boolean value that will tell this method
                                 to return the raw list data.

            Returns:
                object: An instance of the child object that called.
                If a bad request is made then an empty resource object is
                returned.
                -or-
                raw data: If raw_data is true this will return the data that
                          was returned from the request.
        """
        instance = params.pop('instance', cls())
        raw_data = params.pop('raw_data', False)

        response = requests.request(
            "GET",
            instance._make_url(resource_id, *ext),
            headers=instance._default_headers,
            params=params
        )

        if not response.ok:
            raise_response_error(response)

        data = json.loads(response.text)

        return data if raw_data else instance._construct(**data)

    def _get_missing_attrs(self):
        """
        Fills in any missing attributes in an object. List and Retrieve
        can return different attributes so this fills all attributes that are
        missing when a missing attribute is requested.
        """
        data = self.retrieve(self._get_object_id, raw_data=True)

        for attr in data:
            setattr(self, attr, data.get(attr, None))
