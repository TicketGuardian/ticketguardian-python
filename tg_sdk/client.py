from tg_sdk.abstract.list_resource import ListResourcesMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin
from tg_sdk.affiliate import Affiliate


class Client(ListResourcesMixin, RetrieveResourceMixin,):
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
    _updated = False

    @property
    def affiliate(self):
        return Affiliate.retrieve(
            self._affiliate['id'],
            **self.credentials
        )

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
        return self._settings
