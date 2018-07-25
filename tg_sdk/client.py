from tg_sdk.affiliate import Affiliate
from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.post_resource import PostResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Client(ListResourceMixin, RetrieveResourceMixin, PostResourceMixin, ):
    resource = "clients"

    @property
    def external_id(self):
        return self._external_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    @property
    def is_rev_share(self):
        return self._is_rev_share

    @property
    def affiliate(self):
        if not hasattr(self._affiliate, 'resource'):
            self._affiliate = Affiliate.construct(
                id=self._affiliate.id,
                name=self._affiliate.name
            )
        return self._affiliate

    @property
    def domain(self):
        # TODO(Justin): Find an elegant way to get the domain for a Client
        #               The problem is that domain in included on list calls
        #               but is not on single retrieves
        return self._domain

    @property
    def logo(self):
        return self._logo

    @property
    def ui_mode(self):
        return self._ui_mode

    @property
    def settings(self):
        return self._settings
