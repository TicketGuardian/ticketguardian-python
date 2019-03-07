from ticketguardian.abstract import APIResource
from ticketguardian.customer import Customer


class Item(APIResource):
    resource = 'items'

    @property
    def customer(self):
        if self._customer is not None:
            return Customer._construct(**self._customer)
