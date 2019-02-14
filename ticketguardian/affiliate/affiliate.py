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

    def get_parent_scope(self):
        """
        Used to gets all parents within the scope of the Affiliate.
        Returns:
            list: a list of all parents of the Affiliate
        """
        result = []
        affiliate = self.parent

        while affiliate is not None:
            result += [affiliate]
            affiliate = affiliate.parent

        return result
