from ticketguardian.affiliate import Affiliate
from ticketguardian.abstract import (
    ListResourceMixin,
    PostResourceMixin,
    PatchResourceMixin,
    RetrieveResourceMixin, )


class Client(
        ListResourceMixin,
        PatchResourceMixin,
        PostResourceMixin,
        RetrieveResourceMixin,):

    resource = "clients"

    @property
    def affiliate(self):
        if not hasattr(self._affiliate, 'resource'):
            self._affiliate = Affiliate._construct(obj=self._affiliate)
        return self._affiliate

    @property
    def domain(self):
        return

    @property
    def scope(self):
        """
        Used to gets all children within the scope of this Client.
        Returns:
            list: a list of all children of the Client including itself.
        """
        return self.retrieve(self.id, 'scope', raw_data=True)
