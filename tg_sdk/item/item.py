from tg_sdk.customer import Customer
from tg_sdk.abstract import APIResource


class Item(APIResource):
    # Todo(Justin): Add the rest of the functionality to this class
    resource = 'items'

    @property
    def customer(self):
        if self._customer is None:
            return None
        return Customer.construct(**self._customer)
