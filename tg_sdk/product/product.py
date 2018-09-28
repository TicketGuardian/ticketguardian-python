from tg_sdk.abstract import (
    ListResourceMixin,
    RetrieveResourceMixin, )


class Product(RetrieveResourceMixin, ListResourceMixin):
    resource = "products"
