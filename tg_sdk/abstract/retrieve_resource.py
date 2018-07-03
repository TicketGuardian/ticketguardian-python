import requests
import json
from tg_sdk.api_resource import APIResource


class RetrieveResourceMixin(APIResource):

    @classmethod
    def retrieve(cls, resource_id, **params):
        """
        Get a single resource using the child object that called and initialized
        an instance of that child object.
            Arguments:
                resource_id {str} -- The unique id of the resource.
            Returns:
                [object] -- An instance of the child object that called.
        """
        instance = cls()
        super().__init__(instance, **params)
        url = "{}/api/v2/{}/{}/".format(instance.core_url, instance.resource, resource_id)

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

        return super().construct(instance, data)
