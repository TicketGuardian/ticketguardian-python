from ticketguardian.abstract import (
    ListResourceMixin,
    RetrieveResourceMixin, )


class Product(RetrieveResourceMixin, ListResourceMixin):
    resource = "products"

    def __init__(self):
        super(Product, self).__init__()
