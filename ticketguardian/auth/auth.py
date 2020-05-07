from ticketguardian.abstract import RetrieveResourceMixin


class Auth(RetrieveResourceMixin):

    resource = 'auth'

    @classmethod
    def get_parents(cls, affiliate_id):
        """
        Get all parents of an affiliate.

        Returns:
            list -- A list containing all parent ids of the Affiliate.
        """
        affiliate = Affiliate.retrieve(affiliate_id)

        result = []

        while hasattr(affiliate.parent, 'id'):
            try:
                result.append(affiliate.parent.id)
                affiliate = affiliate.parent
            except Exception:
                # Relies on either reaching top affiliate which has a null
                # parent or not having permissions to access top level parent.
                break

        return result

    @classmethod
    def me(cls, **params):
        """
        GET /auth/me/
        returns a dict containing info about the user, with the following keys:
            id, first_name, last_name, email, is_admin, is_superuser,
            external_id, affiliate, client, role
        params:
            1. token (str): JWT token.
                When provided, it will override the instances default headers.
                If you don't provide the token, then it will default to the
                sdk's instantiated token.
        """
        return cls.retrieve('me', raw_data=True, instance=cls(**params))
