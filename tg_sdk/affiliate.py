from tg_sdk.abstract.list_resource import ListResourcesMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourcesMixin, RetrieveResourceMixin,):
    resource = "affiliates"
    id = None
    name = None
    domain = None
    _parent = None
    _settings = None
    _updated = False

    @property
    def parent(self):
        return self.retrieve(
            self._parent['id'],
            **self.credentials
        )

    @property
    def settings(self):
        self.update(self._settings)
        return self._settings

    @settings.setter
    def settings(self, data):
        self._settings = data
