import json
import requests

from tg_sdk.api_resource import APIResource


class ListResourcesMixin(APIResource):

    @classmethod
    def list(cls, **params):
        """
        Retrieve multiple resources and return a list of
        instances of child objects initialized with the data received.
        Any additional filter can be added into params as a keyword arg.
            Arguments:
                resource_id {str} -- The unique id of the resource.

            Keyword Arguments:
                public_key {str} -- The public key for this instance.
                secret_key {str} -- The secret key for this instance.
                limit {int} -- The maximum resources that will be returned

            Returns:
                list -- A list of instances of the child object that called.
        """
        resources = []
        instance = cls()
        super(cls, instance).__init__(**params)
        limit = params.get("limit", None)
        request_limit = min(limit, 1000) if limit else 1000
        parameters = params
        parameters['limit'] = request_limit
        url = "{}/api/v2/{}/".format(
            instance.core_url,
            instance.resource)

        while url and (limit is None or limit > len(resources)):
            response = requests.request(
                "GET",
                url,
                headers=instance.default_headers,
                params=parameters
            )
            if response.ok:
                data = json.loads(response.text)
                for resource in data.get('results', []):
                    instance = cls()
                    super(cls, instance).__init__(**params)
                    super(cls, instance).construct(resource)
                    resources += [instance]
                url = data.get('next')
            else:
                # TODO: ADD ERROR HANDLING
                return []
        return resources[:limit]
