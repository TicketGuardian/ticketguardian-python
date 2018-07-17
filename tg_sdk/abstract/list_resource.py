import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class ListResourceMixin(APIResource):

    def list(self, **params):
        """
        Retrieve multiple resources and return a list of instances of child
        objects initialized with the data received. Any additional filters can
        be added into params as a keyword arg.

            Keyword Arguments:
                limit (int) -- The maximum resources that will be returned

            Returns:
                list -- A list of instances of the child object that called.
                If an error occurs and a bad request is made then an empty
                list is returned.
        """
        resources = []
        limit = params.get("limit", None)
        url = "{}/api/v2/{}/".format(
            self.core_url,
            self.resource
        )

        while url and (limit is None or limit > len(resources)):
            response = requests.request(
                "GET",
                url,
                headers=self.default_headers,
                params=params
            )
            if response.ok:
                data = json.loads(response.text)
                for resource in data.get('results', []):
                    resources += [self.construct(resource)]
                url = data.get('next')
            else:
                # TODO(Justin): ADD ERROR HANDLING
                return []
        return resources[:limit]
