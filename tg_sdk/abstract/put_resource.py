import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class PutResourceMixin(APIResource):
    def update(self, **params):
        """
        Update a currently existing resource.
            Keyword Arguments:
                ext: An extension of the url if extra args are needed.
                     Does not need the leading or trailing '/'.
                id: An optional resource id. If none is given then use the
                    instances id. This should only be used by resource classes.

            Returns:
                An instance of the object that is being updated.
                If a bad request is made then an empty instance of the resource
                object is returned.
        """
        url = self.make_url(params.pop('id', self.id))

        ext = params.pop('ext', None)
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
