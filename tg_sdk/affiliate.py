from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
    resource = "affiliates"
    id = None
    name = None
    _domain = None
    _parent = None
    _settings = None

    @property
    def domain(self):
        self.update(self._domain)
        return self._domain

    @property
    def parent(self):
        if self._parent is None:
            return None
        if not hasattr(self._parent, 'resource'):
            self._parent = self.construct(
                {
                    'id': self._parent.id,
                    'name': self._parent.name
                 }
            )
        return self._parent

    @property
    def settings(self):
        self.update(self._settings)
        return self._settings
