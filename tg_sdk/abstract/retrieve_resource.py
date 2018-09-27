import json
import requests

from tg_sdk.abstract.api_resource import APIResource
from tg_sdk.abstract.error_handling import raise_response_error


class RetrieveResourceMixin(APIResource):
    def __getattr__(self, attr):
        if not self.is_updated:
            self.is_updated = True
            self.get_missing_attrs()
            return object.__getattribute__(self, attr)
        raise AttributeError

    def __repr__(self):
        # Each resource class has a resource class attribute that is the
        # plural of the resource name. So I am removing the last letter s.
        return '<{}: {}>'.format(self.resource[:-1].title(), self.name)

    def __str__(self):
        pass

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
        url = instance._make_url(resource_id, *ext)
        raw_data = params.pop('raw_data', False)
        response = requests.request(
            "GET",
            url,
            headers=instance._default_headers,
            params=params
        )
        if response.ok:
            data = json.loads(response.text)
        else:
            raise_response_error(response)

        if raw_data:
            return data
        else:
            return instance._construct(**data)

    def get_missing_attrs(self):
        """
        Fills in any missing attributes in an object. List and Retrieve
        can return different attributes so this fills all attributes that are
        missing when a missing attribute is requested.
        """
        data = self.retrieve(self.id, raw_data=True)
        for attr in data:
            if '_' + attr not in vars(self):
                # This condition skips all non property method names then
                # checks if a private variable of the same name exists
                setattr(self, attr, data.get(attr, None))
