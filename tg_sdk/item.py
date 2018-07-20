from tg_sdk import Customer
from tg_sdk.abstract.api_resource import APIResource


class Item(APIResource):
    # Todo(Justin): This is barebones for now just so I can have an object to
    #               return from other resource classes. I will add more
    #               functionality to this once I make more progress on those
    #               classes.
    id = None
    name = None
    reference_number = None
    cost = None
    _customer = None

    @property
    def customer(self):
        if self._customer is None:
            # Some items on dev have null customers
            return Customer()
        return Customer().construct(self._customer)
