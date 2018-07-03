from tg_sdk.api_resource import API_Resource
from tg_sdk import core_url
import requests
import json


class Retrieve_single(API_Resource):

    @classmethod
    def Retrieve(cls, item_id, **params):
        """
        Get a single item from the resource of the class that called and initialized
        an instance of the child object.
            Arguments:
                item_id {str} -- The unique id of the item.
            Returns:
                [object] -- An instance of the child object that called.
        """
        instance = cls()
        super().__init__(instance, **params)
        url = "{}/api/v2/{}/{}/".format(core_url, cls.RESOURCE_NAME, item_id)

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
