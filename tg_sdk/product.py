from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Product(RetrieveResourceMixin):
    resource = "products"
    id = None
    code = None
