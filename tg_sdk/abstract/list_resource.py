import json
import requests

from tg_sdk.api_resource import APIResource


class ListResourcesMixin(APIResource):

    @classmethod
    def list(cls, **params):
        """
        Retrieve multiple resources and return a list of
        instances of child objects initialized with the data received.
        Any additional filters can be added into params as a keyword arg.

            Keyword Arguments:
                public_key (str) -- The public key for this instance.
                secret_key (str) -- The secret key for this instance.
                limit (int) -- The maximum resources that will be returned

            Returns:
                list -- A list of instances of the child object that called.
        """
        resources = []
        instance = cls()
        super(cls, instance).__init__(**params)
        parameters = params
        limit = parameters.get("limit", None)
        url = "{}/api/v2/{}/".format(
            instance.core_url,
            instance.resource
        )

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
