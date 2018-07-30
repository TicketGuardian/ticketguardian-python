from tg_sdk import Customer
from tg_sdk.abstract.api_resource import APIResource


class Item(APIResource):
    # Todo(Justin): Finish rest of functionality for this class
    resource = 'items'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def reference_number(self):
        return self._reference_number

    @property
    def cost(self):
        return self._cost

    @property
    def customer(self):
        if self._customer is None:
            return None
        return Customer.construct(**self._customer)

    @property
    def event(self):
        return self._event
