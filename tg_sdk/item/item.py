from tg_sdk.abstract import APIResource
from tg_sdk.customer import Customer


class Item(APIResource):
    resource = 'items'

    @property
    def customer(self):
        if self._customer is not None:
            return Customer._construct(**self._customer)
