import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class RetrieveResourceMixin(APIResource):

    def retrieve(self, resource_id, **params):
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
        url = "{}/api/v2/{}/{}/".format(
            self.core_url,
            self.resource,
            resource_id)

        response = requests.request(
            "GET",
            url,
            headers=self.default_headers,
            params=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            # TODO(Justin): ADD ERROR HANDLING
            data = {}

        return self.construct(data)

    def get_missing_attrs(self):
        """
        Used to fill in any missing attributes in an object. List and Retrieve
        can return different attributes which so this makes another api call.
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
                    self.__setattr__('_' + attr, data[attr])

        else:
            # TODO(Justin): ADD ERROR HANDLING
            return None

    def update(self, val):
        """
        Used to fill in any missing attributes in an object. List and Retrieve
        can return different attributes which so this makes another api call.
            Arguments:
                val  -- The value the user is trying to get. This checks to
                        ensure that the object has already been updated and
                        the value is actually None.
        """
        if not self.updated and self.id and val is None:
            self.updated = True
            self.get_missing_attrs()
