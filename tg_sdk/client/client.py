from tg_sdk.affiliate import Affiliate
from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.post_resource import PostResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Client(ListResourceMixin, RetrieveResourceMixin, PostResourceMixin, ):
    resource = "clients"

    @property
    def affiliate(self):
        if not hasattr(self._affiliate, 'resource'):
            self._affiliate = Affiliate.construct(obj=self._affiliate)
        return self._affiliate

    @property
    def domain(self):
        # TODO(Justin): Find an elegant way to get the domain for a Client
        #               The problem is that domain in included on list calls
        #               but is not on single retrieves
        return self._domain
