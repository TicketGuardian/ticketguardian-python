from ticketguardian.abstract import (
    ListResourceMixin,
    RetrieveResourceMixin, )


class Product(RetrieveResourceMixin, ListResourceMixin):
    resource = "products"
