from tg_sdk.customer import Customer
from tg_sdk.abstract import APIResource


class Item(APIResource):
    resource = 'items'

    @property
    def customer(self):
        if self._customer is None:
            return None
        return Customer._construct(**self._customer)
