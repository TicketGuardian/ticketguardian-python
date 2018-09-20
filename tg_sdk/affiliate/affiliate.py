from abstract.list_resource import ListResourceMixin
from abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
    resource = "affiliates"

    @property
    def parent(self):
        if self._parent is None:
            return None

        if not hasattr(self._parent, 'resource'):
            self._parent = self.construct(obj=self._parent)
        return self._parent
