import requests

from tg_sdk.abstract.api_resource import APIResource


class DeleteResourceMixin(APIResource):
    @classmethod
    def delete(cls, resource_id, ext=None):
        """
        Delete an existing resource.
            Arguments:
                resource_id: The unique id of the resource.
                ext: An extension of the url if extra args are needed.
                     Does not need the leading or trailing '/'.

            Returns:
                If a bad request is made then an exception should be raised.
        """
        instance = cls()
        url = "{}/api/v2/{}/{}/".format(
            instance.core_url,
            instance.resource,
            resource_id
        )

        if ext:
            url += "{}/".format(ext)

        response = requests.delete(
            url,
            headers=instance.default_headers
        )

        if not response.ok:
            # TODO(Justin): ADD ERROR HANDLING
            return
