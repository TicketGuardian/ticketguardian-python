import requests

from ticketguardian.abstract.api_resource import APIResource
from ticketguardian.abstract.error_handling import raise_response_error


class PostResourceMixin(APIResource):
    @classmethod
    def create(cls, *ext, **params):
        """
        Post a new resource with the given parameters.
            Keyword Arguments:
                instance: An instance of the class making the retrieval.
                ext: Strings that are extensions of the url
                     This should only be used from within resource methods.
                raw_data (bool): A boolean value that will tell this method to
                                 return the raw list data.
            Returns:
                An instance of the object that was just posted.
                If a bad request is made then an empty resource object is
                returned.
                -or-
                dict of raw data: If raw_data is true.
        """
        raw_data = params.pop('raw_data', False)
        instance = params.pop('instance', None)

        if not instance:
            instance = cls()

        res = requests.post(
            instance._make_url(*ext),
            headers=instance._default_headers,
            json=params
        )
        if not res.ok:
            raise_response_error(res)

        data = res.json()

        return data if raw_data else instance._construct(
            instance=instance,
            **data)
