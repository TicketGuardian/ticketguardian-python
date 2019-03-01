from ticketguardian.client import Client
from ticketguardian.affiliate import Affiliate
from ticketguardian.abstract import RetrieveResourceMixin


class Auth(RetrieveResourceMixin):

    resource = 'auth'

    @classmethod
    def get_scope(cls, root_type='', root_id=''):
        """
        Get scope of Client, Affiliate, or own scope.

        Arguments:
            root_type {str} -- The type of object the root is.
                               Should be 'Client' or 'Affiliate'.
            root_id {str} -- The resource id of the root.

        Returns:
            list -- A list containing all objects within scope including itself
        """
        if root_type.lower() == 'client':
            return Client.retrieve(root_id).scope
        elif root_type.lower() == 'affiliate':
            return Affiliate.retrieve(root_id).scope
        else:
            return cls.retrieve('scope', raw_data=True)
