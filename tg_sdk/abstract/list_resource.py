import json
import requests

from tg_sdk.abstract.api_resource import APIResource


class ListResourcesMixin(APIResource):

    @classmethod
    def list(cls, public_key=None, secret_key=None, env=None, **params):
        """
        Retrieve multiple resources and return a list of instances of child
        objects initialized with the data received. Any additional filters can
        be added into params as a keyword arg.

            Keyword Arguments:
                limit (int) -- The maximum resources that will be returned
                public_key (str) -- The public key for this instance.
                secret_key (str) -- The secret key for this instance.
                env (str) -- The tg_sdk constant of the environment to use.
                             Billing and Core will be in the same env.
                             Prod will always be default.

            Returns:
                list -- A list of instances of the child object that called.
        """
        resources = []
        instance = cls()
        super(cls, instance).__init__(
            public_key=public_key,
            secret_key=secret_key,
            env=env
        )
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
                    super(cls, instance).__init__(
                        public_key=public_key,
                        secret_key=secret_key,
                        env=env
                    )
                    super(cls, instance).construct(resource)
                    resources += [instance]
                url = data.get('next')
            else:
                # TODO(Justin): ADD ERROR HANDLING
                return []
        return resources[:limit]
