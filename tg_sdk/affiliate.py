from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
    resource = "affiliates"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def domain(self):
        return self._domain

    @property
    def parent(self):
        if self._parent is None:
            return None

        if not hasattr(self._parent, 'resource'):
            self._parent = self.construct(
                id=self._parent.id,
                name=self._parent.name
            )
        return self._parent

    @property
    def settings(self):
        return self._settings
