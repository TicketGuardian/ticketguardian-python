from ticketguardian.affiliate import Affiliate
from ticketguardian.abstract import (
    ListResourceMixin,
    PostResourceMixin,
    RetrieveResourceMixin, )


class Client(ListResourceMixin, RetrieveResourceMixin, PostResourceMixin, ):
    resource = "clients"

    @property
    def affiliate(self):
        if not hasattr(self._affiliate, 'resource'):
            self._affiliate = Affiliate._construct(obj=self._affiliate)
        return self._affiliate

    @property
    def domain(self):
        return
