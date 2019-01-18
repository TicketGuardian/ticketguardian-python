import requests

from ticketguardian.abstract.api_resource import APIResource
from ticketguardian.abstract.error_handling import raise_response_error


class DeleteResourceMixin(APIResource):
    @classmethod
    def delete(cls, resource_id, *ext):
        """
        Delete an existing resource.
            Arguments:
                resource_id (str): The unique id of the resource.
                ext (list): An extension of the url if extra args are needed.
                     Does not need the leading or trailing '/'.

            Returns:
                If a bad request is made then an exception should be raised.
        """
        instance = cls()
        url = instance._make_url(resource_id, *ext)
        response = requests.delete(url, headers=instance._default_headers)

        if not response.ok:
            raise_response_error(response)
