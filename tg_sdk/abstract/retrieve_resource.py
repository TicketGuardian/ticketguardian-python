import json
import requests
from tg_sdk.api_resource import APIResource


class RetrieveResourceMixin(APIResource):

    @classmethod
    def retrieve(cls, resource_id, **params):
        """
        Retrieve a single resource and initialize an
        instance of the child object that called.
            Arguments:
                resource_id {str} -- The unique id of the resource.

            Keyword Arguments:
                public_key {str} -- The public key for this instance.
                secret_key {str} -- The secret key for this instance.
                core_url {str} -- The url where requests will be made to.
                billing_url {str} -- The billing url where
                                     requests will be made to.

            Returns:
                [object] -- An instance of the child object that called.
        """
        instance = cls()
        super(cls, instance).__init__(**params)
        url = "{}/api/v2/{}/{}/".format(
                                        instance.core_url,
                                        instance.resource,
                                        resource_id)

        response = requests.request(
            "GET",
            url,
            headers=instance.default_headers,
            params=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            # TODO: ADD ERROR HANDLING
            return cls()

        return super(cls, instance).construct(data)
