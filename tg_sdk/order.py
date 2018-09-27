from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.post_resource import PostResourceMixin
from tg_sdk.abstract.put_resource import PutResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin
from tg_sdk.client import Client
from tg_sdk.customer import Customer
from tg_sdk.item import Item
from tg_sdk.policy import Policy


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
            self._client = Client._construct(id=self._client)
        return self._client

    @property
    def customer(self):
        if self._customer is None:
            return None
        return Customer._construct(obj=self._customer)

    @property
    def items(self):
        if len(self._items) > 0 and isinstance(self._items[0], dict):
            self._items = self._construct_list(self._items, Item)
        return self._items

    @property
    def policies(self):
        if len(self._policies) > 0 and isinstance(self._policies[0], dict):
            self._policies = self._construct_list(self._policies, Policy)
        return self._policies

    @property
    def quote(self):
        # TODO(Justin): IMPLEMENT WHEN QUOTE CLASS IS CREATED
        return

    def add_items(self, currency="USD", **params):
        """Add items to the order instance using the given parameters.

        Keyword Arguments:
            currency (str): The currency of the Items. Defaults to USD.
            items (list): The list of item dictionaries.
                item (dict): a dictionary containing the following values.
                   Name (str): The name of the item.
                   reference_number (str): The unique number of the item.
                   cost (float): The cost of the item.
                   customer (dict): An optional customer object.
                                    Defaults to null.
                   event (dict): An optional event object.
                                 Defaults to null.

        Returns:
            The order object that the items were added to.
        """
        if self.order_number is None or params == {}:
            # TODO(Justin): Error handling
            return None

        return self.update(self.order_number, 'add-items', **params)
