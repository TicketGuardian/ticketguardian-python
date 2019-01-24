from ticketguardian.affiliate import Affiliate
from ticketguardian.abstract import (
    APIResource,
    ListResourceMixin,
    PostResourceMixin,
    RetrieveResourceMixin, )


class Client(ListResourceMixin, RetrieveResourceMixin, PostResourceMixin, ):
    resource = "clients"
    
    def __init__(self):
        super(Client, self).__init__()


    @property
    def affiliate(self):
        if not hasattr(self._affiliate, 'resource'):
            self._affiliate = Affiliate._construct(obj=self._affiliate)
        return self._affiliate

    @property
    def domain(self):
        return
