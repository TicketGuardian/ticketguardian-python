import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class ListResourceMixin(APIResource):
    @classmethod
    def list(cls, **params):
        """
        Retrieve multiple resources and return a list of instances of child
        objects initialized with the data received. Any additional filters can
        be added into params as a keyword arg.

            Keyword Arguments:
                limit: The maximum resources that will be returned

            Returns:
                list: A list of instances of the child object that called.
                If an error occurs or a bad request is made then an empty
                list is returned.
        """
        instance = cls()
        resources = []
        limit = params.get("limit", None)
        url = "{}/api/v2/{}/".format(
            instance.core_url,
            instance.resource
        )

        while url and (limit is None or limit > len(resources)):
            response = requests.request(
                "GET",
                url,
                headers=instance.default_headers,
                params=params
            )
            if response.ok:
                data = json.loads(response.text)
                resources += [
                    instance.construct(**res) for res in data.get('results',[])
                ]
                url = data.get('next')
            else:
                # TODO(Justin): ADD ERROR HANDLING
                return []
        return resources[:limit]

    def list_raw(self, ext=None, **params):
        """
        Retrieve multiple resources and return a list of raw data.
        Any additional filters can be added into params as a keyword arg.

            Keyword Arguments:
                limit: The maximum resources that will be returned.
                ext: The extension of the url if needed.

            Returns:
                list: A list of instances of the child object that called.
                If an error occurs or a bad request is made then an empty
                list is returned.
        """
        resources = []
        limit = params.get("limit", None)
        url = "{}/api/v2/{}/{}/".format(
            self.core_url,
            self.resource,
            self.id
        )

        if ext:
            url += "{}/".format(ext)

        while url and (limit is None or limit > len(resources)):
            response = requests.request(
                "GET",
                url,
                headers=self.default_headers,
                params=params
            )
            if response.ok:
                data = json.loads(response.text)
                resources += [res for res in data.get('results', [])]
                url = data.get('next')
            else:
                # TODO(Justin): ADD ERROR HANDLING
                return []
        return resources[:limit]
