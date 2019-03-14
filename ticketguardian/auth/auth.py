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
