from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
    resource = "affiliates"

    @property
    def parent(self):
        if self._parent is None:
            return None

        if not hasattr(self._parent, 'resource'):
            self._parent = self._construct(obj=self._parent)
        return self._parent
