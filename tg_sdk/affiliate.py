from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
    resource = "affiliates"
    id = None
    name = None
    domain = None
    _parent = None
    _settings = None

    @property
    def parent(self):
        if isinstance(self._parent, dict):
            self._parent = self.retrieve(
                self._parent['id'],
                **self.credentials
            )
        return self._parent

    @property
    def settings(self):
        self.update(self._settings)
        if isinstance(self._settings, dict):
            self._settings = super().construct_general(
                'Settings',
                self._settings
            )
        return self._settings
