from tg_sdk.client import Client
from tg_sdk.customer import Customer
from tg_sdk.item import Item
from tg_sdk.policy import Policy
from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.post_resource import PostResourceMixin
from tg_sdk.abstract.put_resource import PutResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Order(
    ListResourceMixin,
    RetrieveResouMixin,
    PostResourceMixin,
    PutResourceMixin, ):

    resource = "orders"

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

    @property
    def order_number(self):
        return self._order_number

    @property
    def subtotal(self):
        return self._subtotal

    @property
    def currency(self):
        return self._currency

    @property
    def id(self):
        return self.order_number

    @property
    def attrs(self):
        return self._attrs

    @property
    def client(self):
        if self._client is None:
            return None
        if isinstance(self._client, str):
            self._client = Client.construct(id=self._client)
        return self._client

    @property
    def customer(self):
        if self._customer is None:
            return None
        return Customer.construct(
            id=self._customer.id,
            email=self._customer.email,
            first_name=self._customer.first_name,
            last_name=self._customer.last_name
        )

    @property
    def items(self):
        if len(self._items) > 0 and isinstance(self._items[0], dict):
            self._items = self.construct_list(self._items, Item)
        return self._items

    @property
    def policies(self):
        if len(self._policies) > 0 and isinstance(self._policies[0], dict):
            self._policies = self.construct_list(self._policies, Policy)
        return self._policies

    @property
    def quote(self):
        # TODO(Justin): IMPLEMENT WHEN QUOTE CLASS IS CREATED
        return

    def add_items(self, **params):
        # TODO(Justin): Using PUT should not return a new instance but should
        #               update the existing instance that was used to call.
        if self.order_number is None or params == {}:
            # TODO(Justin): Error handling
            return None

        return self.put(self.order_number, ext='add-items', **params)
