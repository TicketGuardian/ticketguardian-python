from tg_sdk.abstract import RetrieveResourceMixin


class Customer(RetrieveResourceMixin):
    resource = 'customers'
