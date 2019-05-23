from ticketguardian.abstract import RetrieveResourceMixin


class Auth(RetrieveResourceMixin):

    resource = 'auth'

    def get_scope(self):
        """
        Get own scope.

        Returns:
            list -- A list containing all objects within scope including self
        """
        return self.retrieve('scope', raw_data=True, instance=self)

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
