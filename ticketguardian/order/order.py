from ticketguardian.abstract import (
    ListResourceMixin,
    PostResourceMixin,
    PutResourceMixin,
    RetrieveResourceMixin, )
from ticketguardian.client import Client
from ticketguardian.customer import Customer
from ticketguardian.item import Item
from ticketguardian.policy import Policy
from ticketguardian._project import _validate
from ticketguardian.order import exceptions


class Order(
        ListResourceMixin,
        RetrieveResourceMixin,
        PostResourceMixin,
        PutResourceMixin, ):

    resource = "orders"

    @property
    def id(self):
        return self.order_number

    @property
    def client(self):
        if self._client is not None and isinstance(self._client, str):
            self._client = Client._construct(id=self._client)
        return self._client

    @property
    def customer(self):
        if self._customer is not None and not hasattr(
                self._customer, 'resource'):
            self._customer = Customer._construct(obj=self._customer)
        return self._customer

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

    def charge(self, customer, billing_address, card, policies=[]):
        """ Chage an order.

        Keyword Arguments:
            customer (dict): Must include first_name, last_name, email, phone
            billing_address (dict): The order's billing address.
                                    Must include address1, address2, city,
                                    state, country, zip_code.
            card (dict): Card must contain the 'number', 'expire_month',
                         and 'expire_year'.

        Optional Arguments:
            policies (list): A list of Policy Numbers. If none are given then
                             all policies are charged.

        Returns:
            An object containing the information returned from the charge.
            The order that was charged is updated to reflect the changes.
        """
        _validate._validate_customer(customer)
        _validate._validate_card(card)
        _validate._validate_address(billing_address)

        response = super().create(
            self.order_number,
            'charge',
            customer=customer,
            billing_address=billing_address,
            card=card,
            policies=policies,
            raw_data=True)

        self._get_missing_attrs()

        return self._construct_general('Charge', response)

    def add_items(self, items, currency='USD', **params):
        """Add items to the order instance using the given parameters.

        Keyword Arguments:
            items (list): The list of item dictionaries.
                item (dict): a dictionary containing the following values.
                   name (str): The name of the item.
                   reference_number (str): The unique number of the item.
                   cost (float): The cost of the item.
                   customer (dict): An optional customer object.
                                    Defaults to null.
                   event (dict): An optional event object.
                                 Defaults to null.

        Optional Keyword Arguments:
            currency (str): The currency of the Items. Defaults to USD.
            card (dict): Card must contain the 'number', 'expire_month',
                         and 'expire_year'.

        Returns:
            The order object that the items were added to.
        """
        if not isinstance(items, list) or len(items) == 0:
            raise exceptions.InvalidItemsException

        if params.get('card'):
            _validate._validate_card(params.get('card'))

        return self.update(
            self.order_number,
            'add-items',
            items=items,
            currency=currency,
            **params)

    @classmethod
    def create(cls, items, customer, order_number, **params):
        """
        Create an order using the following parameters.

        Keyword Arguments:
            items (list): The list of item objects.
                item (dict): a dictionary containing the following values.
                   name (str): The name of the item.
                   reference_number (str): The unique number of the item.
                   cost (float): The cost of the item.
                   customer (dict): An optional customer object.
                                    Must include first_name, last_name, email.
                                    Defaults to null.
                   event (dict): An optional event object.
                                 Defaults to null.
            customer (dict): The order level customer object.
                             Must include first_name, last_name, email.
            order_number (str or int): A unique id for the order.

        Optional Keyword Arguments:
            card (dict): Card must contain the 'number', 'expire_month',
                         and 'expire_year'.
            currency (str): The currency of the Items. Defaults to USD.
            http_referrer (str): The clients IP.
            tracking (dict): An object containing the tracking information.
                             Must include carrier and tracking_number.
            shipping_address (dict): The order's shipping address.
                                     Must include address1, address2, city,
                                     state, country, zip_code.
                                     Defaults to billing_address.
            billing_address (dict): The order's billing address.
                                    Must include address1, address2, city,
                                    state, country, zip_code.

        Returns:
            The order object that was created.
        """
        if not isinstance(items, list) or len(items) == 0:
            raise exceptions.InvalidItemsException
        if {"first_name", "last_name", "email"} != set(customer.keys()):
            raise exceptions.InvalidCustomerInformationException
        if params.get('card'):
            _validate._validate_card(params.get('card'))

        if params.get('billing_address'):
            _validate._validate_address(params['billing_address'])

        if params.get('shipping_address'):
            _validate._validate_address(params['shipping_address'])
        elif params.get('billing_address'):
            params['ship_to_billing_addr'] = True

        return super(Order, cls).create(
            items=items,
            customer=customer,
            order_number=order_number,
            **params)
