from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin
from tg_sdk.item import Item


class Policy(RetrieveResourceMixin):
    resource = 'policies'
    id_name = 'policy_number'

    @property
    def item(self):
        if not hasattr(self._item, 'resource'):
            self._item = Item._construct(obj=self._item)
        return self._item

    @property
    def customer(self):
        if not hasattr(self._customer, 'resource'):
            self._item = Item._construct(obj=self._item)
        return self._customer
