from tg_sdk import Client, Customer, Item, Policy
from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.post_resource import PostResourceMixin
from tg_sdk.abstract.put_resource import PutResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Order(
    ListResourceMixin,
    RetrieveResourceMixin,
    PostResourceMixin,
    PutResourceMixin, ):

    resource = "orders"
    created = None
    updated = None
    order_number = None
    subtotal = None
    currency = None
    _client = None
    _items = None
    _policies = None
    _customer = None
    _attrs = None

    @property
    def attrs(self):
        self.update(self._attrs)
        return self._attrs

    @property
    def client(self):
        self.update(self._client)
        if isinstance(self._client, str):
            self._client = Client.retrieve(self._client)
        return self._client

    @property
    def customer(self):
        return Customer.construct(self._customer)

    @property
    def items(self):
        # Is it necessary to create an object for every item when
        # This property is called? or should I make the object
        # just for the specific item they request.
        self.update(self._items)
        if len(self._items) > 0 and isinstance(self._items[0], dict):
            for i in range(len(self._items)):
                self._items[i] = Item().construct(self._items[i])
            return self._items

    @property
    def policies(self):
        # Is it necessary to create an object for every item when
        # This property is called? or should I make the object
        # just for the specific item they request.
        self.update(self._policies)
        if len(self._policies) > 0 and isinstance(self._policies[0], dict):
            for i in range(len(self._policies)):
                self._policies[i] = Policy().construct(self._policies[i])
        return self._policies

    @property
    def quote(self):
        # TODO(Justin): IMPLEMENT WHEN QUOTE CLASS IS CREATED
        return

    def add_items(self, order_id=None, **params):
        if order_id is None:
            if self.order_number is not None:
                order_id = self.order_number
            else:
                # TODO(Justin): Error handling
                return None

        return self.put(order_id, ext='add-items', **params)
