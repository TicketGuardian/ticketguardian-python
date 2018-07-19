import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class RetrieveResourceMixin(APIResource):
    @classmethod
    def retrieve(cls, resource_id, **params):
        """
        Retrieve a single resource and initialize an instance of the child
        object that called.

            Arguments:
                resource_id (str) -- The unique id of the resource.

            Returns:
                object -- An instance of the child object that called.
                If a bad request is made then an empty resource object is
                returned.
        """
        instance = cls()
        url = "{}/api/v2/{}/{}/".format(
            instance.core_url,
            instance.resource,
            resource_id)

        response = requests.request(
            "GET",
            url,
            headers=instance.default_headers,
            params=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            # TODO(Justin): ADD ERROR HANDLING
            data = {}

        return instance.construct(data)

    def get_missing_attrs(self):
        """
        Fills in any missing attributes in an object. List and Retrieve
        can return different attributes so this fills all attributes that are
        missing when a missing attribute is requested.
        """
        url = "{}/api/v2/{}/{}/".format(
            self.core_url,
            self.resource,
            self.id
        )

        response = requests.request(
            "GET",
            url,
            headers=self.default_headers,
        )

        if response.ok:
            data = json.loads(response.text)
            for attr in data:
                if not getattr(self, '_' + attr, True):
                    setattr(self, '_' + attr, data[attr])

        else:
            # TODO(Justin): ADD ERROR HANDLING
            return None

    def update(self, val):
        """
        Checks if the object has already been updated or not. Some values in
        the object are None so this ensures that api calls will not be made
        multiple times to retrieve a value that is None.
            Arguments:
                val  -- The value the user is trying to get.
        """
        if not self.updated and self.id and val is None:
            self.updated = True
            self.get_missing_attrs()
