from abstract.list_resource import ListResourceMixin
from abstract.retrieve_resource import RetrieveResourceMixin


class Product(RetrieveResourceMixin, ListResourceMixin):
    resource = "products"
