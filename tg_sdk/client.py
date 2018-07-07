from tg_sdk.abstract.list_resource import ListResourcesMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Client(ListResourcesMixin, RetrieveResourceMixin,):
    resource = "clients"
    external_id = None
    id = None
    name = None
    status = None
    is_rev_share = None
    affiliate = None
    _domain = None
    _logo = None
    _ui_mode = None
    _settings = None
    _updated = False

    @property
    def domain(self):
        # TODO(Justin): Find an elegant way to get the domain for a Client
        #               The problem is that domain in included on list calls
        #               but is not on single retrieves
        return self._domain

    @domain.setter
    def domain(self, data):
        self._domain = data

    @property
    def logo(self):
        self.update(self._logo)
        return self._logo

    @logo.setter
    def logo(self, data):
        self._logo = data

    @property
    def ui_mode(self):
        self.update(self._ui_mode)
        return self._ui_mode

    @ui_mode.setter
    def ui_mode(self, data):
        self._ui_mode = data

    @property
    def settings(self):
        self.update(self._settings)
        return self._settings

    @settings.setter
    def settings(self, data):
        self._settings = data
