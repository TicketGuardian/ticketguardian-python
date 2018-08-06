from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Product(RetrieveResourceMixin, ListResourceMixin):
    resource = "products"
