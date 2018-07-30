from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin
from tg_sdk.item import Item


class Policy(RetrieveResourceMixin):
    # Todo(Justin): Finish rest of functionality for this class
    resource = 'policies'

    @property
    def item(self):
        if not hasattr(self._item, 'resource'):
            self._item = Item.construct(
                reference_number=self._item.reference_number,
                cost=self._item.cost,
                id=self._item.id,
                name=self._item.name
            )
        return self._item

    @property
    def customer(self):
        if not hasattr(self._customer, 'resource'):
            self._item = Item.construct(
                reference_number=self._item.reference_number,
                cost=self._item.cost,
                id=self._item.id,
                name=self._item.name
            )
        return self._customer

    @property
    def policy_number(self):
        return self._policy_number

    @property
    def premium(self):
        return self._premium

    @property
    def coverage_amount(self):
        return self._coverage_amount

    @property
    def currency(self):
        return self._currency

    @property
    def id(self):
        return self._policy_number

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated
