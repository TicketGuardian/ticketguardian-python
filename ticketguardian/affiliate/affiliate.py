from ticketguardian.abstract import (
    ListResourceMixin,
    RetrieveResourceMixin, )


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
    resource = "affiliates"

    @property
    def parent(self):
        if self._parent is not None and not hasattr(self._parent, 'resource'):
            self._parent = self._construct(obj=self._parent)
        return self._parent
