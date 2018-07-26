from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Customer(RetrieveResourceMixin,):
    # Todo(Justin): Finish rest of functionality for this class
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
