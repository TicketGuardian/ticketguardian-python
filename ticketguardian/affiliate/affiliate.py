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

    @property
    def scope(self):
        """
        Used to gets all children within the scope of this Affiliate.
        Returns:
            list: a list of all children of the Affiliate
        """
        return self.retrieve(self.id, 'scope', raw_data=True)

    def get_parent_scope(self):
        """
        Used to gets all parents within the scope of this Affiliate.
        Returns:
            list: a list of all parents of the Affiliate
        """
        result = []
        affiliate = self.parent

        while affiliate is not None:
            result += [affiliate]
            affiliate = affiliate.parent

        return result
