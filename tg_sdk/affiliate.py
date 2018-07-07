from tg_sdk.abstract.list_resource import ListResourcesMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourcesMixin, RetrieveResourceMixin,):
    resource = "affiliates"
    id = None
    name = None
    domain = None
    parent = None
    _settings = None
    _updated = False

    @property
    def settings(self):
        self.update(self._settings)
        return self._settings

    @settings.setter
    def settings(self, data):
        self._settings = data