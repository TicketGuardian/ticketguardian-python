from ticketguardian.abstract import (
    PostResourceMixin,
    RetrieveResourceMixin,
)


class Customer(
    PostResourceMixin,
    RetrieveResourceMixin):
    resource = 'customers'
