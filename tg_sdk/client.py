from tg_sdk.affiliate import Affiliate
from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.post_resource import PostResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Client(ListResourceMixin, RetrieveResourceMixin, PostResourceMixin, ):
    resource = "clients"
    external_id = None
    id = None
    name = None
    status = None
    is_rev_share = None
    _affiliate = None
    _domain = None
    _logo = None
    _ui_mode = None
    _settings = None

    @property
    def affiliate(self):
        if isinstance(self._affiliate, dict):
            self._affiliate = Affiliate(**self.credentials).retrieve(
                self._affiliate['id']
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
        self.update(self._logo)
        return self._logo

    @property
    def ui_mode(self):
        self.update(self._ui_mode)
        return self._ui_mode

    @property
    def settings(self):
        self.update(self._settings)
        if isinstance(self._settings, dict):
            self._settings = super().construct_general(
                'Settings',
                self._settings
            )
        return self._settings
