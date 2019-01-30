from ticketguardian.abstract import (
    ListResourceMixin,
    PatchResourceMixin,
    RetrieveResourceMixin, )


class Affiliate(
    ListResourceMixin,
    PatchResourceMixin,
    RetrieveResourceMixin,):
    resource = "affiliates"

    def __init__(self):
        super(Affiliate, self).__init__()

    @property
    def parent(self):
        if self._parent is not None and not hasattr(self._parent, 'resource'):
            self._parent = self._construct(obj=self._parent)
        return self._parent
