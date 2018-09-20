from abstract.list_resource import ListResourceMixin
from abstract.post_resource import PostResourceMixin
from abstract.put_resource import PutResourceMixin
from abstract.retrieve_resource import RetrieveResourceMixin
from client import Client
from customer import Customer
from item import Item
from policy import Policy


class Order(
        ListResourceMixin,
        RetrieveResourceMixin,
        PostResourceMixin,
        PutResourceMixin, ):

    resource = "orders"

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
        return Customer.construct(obj=self._customer)

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

        return self.update(self.order_number, 'add-items', **params)
