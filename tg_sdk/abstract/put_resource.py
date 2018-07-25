import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class PutResourceMixin(APIResource):
    @classmethod
    def put(cls, resource_id, ext=None, **params):
        """
        Update a currently existing resource.
            Arguments:
                resource_id: The unique id of the resource.
                ext: An extension of the url if extra args are needed.
                     Does not need the leading or trailing '/'.

            Returns:
                An instance of the object that is being updated.
                If a bad request is made then an empty instance of the resource
                object is returned.
        """
        instance = cls()
        url = "{}/api/v2/{}/{}/".format(
            instance.core_url,
            instance.resource,
            resource_id
        )

        if ext:
            url += "{}/".format(ext)

        response = requests.put(
            url,
            headers=instance.default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            # TODO(Justin): ADD ERROR HANDLING
            data = {}

        return instance.construct(data)
