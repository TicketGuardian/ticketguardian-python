from ticketguardian.abstract import (
    PostResourceMixin,
    RetrieveResourceMixin,
)


class Customer(
    PostResourceMixin,
    RetrieveResourceMixin):
    resource = 'customers'

    def __init__(self):
        super(Customer, self).__init__()
