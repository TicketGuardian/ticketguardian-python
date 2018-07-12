from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
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
