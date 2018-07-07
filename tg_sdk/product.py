from tg_sdk.abstract.list_resource import ListResourcesMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Product(RetrieveResourceMixin, ListResourcesMixin):
    resource = "products"
    id = None
    code = None
