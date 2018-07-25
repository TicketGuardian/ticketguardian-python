import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class PutResourceMixin(APIResource):
    def put(self, resource_id, ext=None, **params):
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
        url = "{}/api/v2/{}/{}/".format(
            self.core_url,
            self.resource,
            resource_id
        )

        if ext:
            url += "{}/".format(ext)

        response = requests.put(
            url,
            headers=self.default_headers,
            json=params
        )

        if response.ok:
            data = json.loads(response.text)
            for key in data:
                setattr(self, '_' + key, data[key])
        else:
            # TODO(Justin): ADD ERROR HANDLING
            return
