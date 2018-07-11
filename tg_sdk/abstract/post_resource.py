import requests

from tg_sdk.api_resource import APIResource


class PostResourceMixin(APIResource):

    @classmethod
    def post(cls, public_key=None, secret_key=None, env=None, **params):
        """
        Post a new resource with the given parameters.

            Keyword Arguments:
                public_key (str) -- The public key for this instance.
                secret_key (str) -- The secret key for this instance.
                env (str) -- The str of the environment this will be posted to.
                             'dev', 'sandbox', or 'prod'
                              prod is always default.
        """
        instance = cls(
            public_key=public_key,
            secret_key=secret_key,
            env=env
        )

        url = "{}/api/v2/{}/".format(
            instance.core_url,
            instance.resource
        )

        response = requests.post(
            url,
            headers=instance.default_headers,
            json=params
        )

        if not response.ok:
            # TODO(Justin): ADD ERROR HANDLING
            pass
