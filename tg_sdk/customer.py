from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Customer(RetrieveResourceMixin,):
    # Todo(Justin): This is barebones for now just so I can have an object to
    #               return from other resource classes. I will add more
    #               functionality to this once I make more progress on those
    #               classes.
    resource = 'customers'

    @property
    def id(self):
        return self._id

    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone(self):
        return self._phone

    @property
    def shipping_address(self):
        return self._shipping_address

    @property
    def billing_address(self):
        return self._billing_address
