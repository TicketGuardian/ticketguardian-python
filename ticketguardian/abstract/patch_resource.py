import requests

from ticketguardian.abstract.api_resource import APIResource
from ticketguardian.abstract.error_handling import raise_response_error


class PatchResourceMixin(APIResource):
    def patch(self, resource_id, *ext, **params):
        """
        Update a currently existing resource.
            Keyword Arguments:
                ext: An extension of the url if extra args are needed.
                     Does not need the leading or trailing '/'.

            Returns:
                An instance of the object that is being updated.
                If a bad request is made then an empty instance of the resource
                object is returned.
        """
        return self.partial_update(request, *args, **kwargs)