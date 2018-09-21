from tg_sdk.abstract import (
    ListResourceMixin,
    RetrieveResourceMixin, )


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
    resource = "affiliates"

    @property
    def parent(self):
        if self._parent is None:
            return None

        if not hasattr(self._parent, 'resource'):
            self._parent = self.construct(obj=self._parent)
        return self._parent
