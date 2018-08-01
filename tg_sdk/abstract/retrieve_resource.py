import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class RetrieveResourceMixin(APIResource):
    def __getattr__(self, attr):
        if attr[0] == '_' and attr[1:] in type(self).__dict__:
            self.get_missing_attrs()
            return object.__getattribute__(self, attr)
        # TODO(Justin): Revisit when adding error handling
        #               Figure out if this should raise a custom Exception or
        #               an AttributeError.
        return None

    @classmethod
    def retrieve(cls, resource_id, **params):
        """
        Retrieve a single resource and initialize an instance of the child
        object that called.

            Arguments:
                resource_id: The unique id of the resource.

            Returns:
                object: An instance of the child object that called.
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

    def retrieve_raw(self, ext=None, **params):
        """
        Retrieve a single resource but return the raw data instead of
        constructing new instance. There are a few cases where resource classes
        need to make requests that does not require a new instance.

            Returns:
                The raw data of the response
        """
        url = "{}/api/v2/{}/{}/".format(
            self.core_url,
            self.resource,
            self.id
        )

        if ext:
            url += "{}/".format(ext)

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
        return data

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
                # Use type(self).__dict__ to iterate through all property
                # method names
                if attr[0] != '_' and ('_' + attr) not in self.__dict__:
                    # This condition skips all non property method names then
                    # checks if a private variable of the same name exists
                    setattr(self, '_' + attr, data.get(attr, None))

        else:
            # TODO(Justin): ADD ERROR HANDLING
            return None
