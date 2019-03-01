from ticketguardian.abstract import APIResource
from ticketguardian.customer import Customer


class Item(APIResource):
    resource = 'items'

    def __init__(self):
        super(Item, self).__init__()

    @property
    def customer(self):
        if self._customer is not None:
            return Customer._construct(**self._customer)
