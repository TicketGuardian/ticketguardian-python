import requests

from tg_sdk.api_resource import APIResource


class PostResource(APIResource):

    @classmethod
    def post(cls, **params):
        """
        Post a new resource with the given parameters.
        Keyword Arguments:
                public_key {str} -- The public key for this instance.
                secret_key {str} -- The secret key for this instance.
                env {str} -- The str of the environment this will be posted to.
                             'dev', 'sandbox', or 'prod'
                              prod is always default.
        """
        instance = cls(**params)

        url = "{}/api/v2/{}/".format(
            instance.core_url,
            instance.resource
        )

        response = requests.post(
            url,
            headers=instance.default_headers,
            json=cls._make_payload(**params)
        )

        if response.ok:
            print('ok')
        else:
            # TODO(Justin): ADD ERROR HANDLING
            print('not ok')

    def _make_payload(**params):
        check = {
            'public_key': 0,
            'secret_key': 0,
            'env': 0
        }
        payload = {}
        for key in params:
            if key not in check:
                payload[key] = params[key]

        return payload
