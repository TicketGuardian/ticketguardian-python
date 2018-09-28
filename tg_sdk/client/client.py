from tg_sdk.affiliate import Affiliate
from tg_sdk.abstract import (
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
