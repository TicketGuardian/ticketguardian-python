from tg_sdk.abstract.retrieve_resource import Retrieve_single


class Product(Retrieve_single):
    RESOURCE_NAME = "products"
    id = None
    code = None

