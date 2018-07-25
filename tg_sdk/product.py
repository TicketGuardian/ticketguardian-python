from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Product(RetrieveResourceMixin, ListResourceMixin):
    resource = "products"

    @property
    def id(self):
        return self._id

    @property
    def code(self):
        return self._code

    @property
    def label(self):
        return self._label

    @property
    def name(self):
        return self._name
