import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class RetrieveResourceMixin(APIResource):
    def __getattr__(self, attr):
        if attr[0] == '_' and attr[1:] in type(self).__dict__:
            self.get_missing_attrs()
            return object.__getattribute__(self, attr)
        return None

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
        return instance.construct(**data)

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
            for attr in type(self).__dict__:
                if attr[0] != '_' and ('_' + attr) not in self.__dict__:
                    setattr(self, '_' + attr, data.get(attr, None))

        else:
            # TODO(Justin): ADD ERROR HANDLING
            return None
