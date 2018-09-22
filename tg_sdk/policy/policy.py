from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin
from tg_sdk.item import Item


class Policy(RetrieveResourceMixin):
    # Todo(Justin): Add the rest of the functionality to this class
    resource = 'policies'
    id_name = 'policy_number'

    @property
    def item(self):
        if not hasattr(self._item, 'resource'):
            self._item = Item.construct(obj=self._item)
        return self._item

    @property
    def customer(self):
        if not hasattr(self._customer, 'resource'):
            self._item = Item.construct(obj=self._item)
        return self._customer
