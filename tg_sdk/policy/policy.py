from tg_sdk.abstract import (
    RetrieveResourceMixin,
    PutResourceMixin,
    ListResourceMixin)
from tg_sdk.item import Item
from tg_sdk.abstract import validate
from tg_sdk.policy.exceptions import NoBillingAddressException
from tg_sdk.policy.constants import UPGRADED


class Policy(
        RetrieveResourceMixin,
        PutResourceMixin,
        ListResourceMixin):

    resource = 'policies'
    id_name = 'policy_number'

    @property
    def item(self):
        if not hasattr(self._item, 'resource'):
            self._item = Item._construct(obj=self._item)
        return self._item

    @property
    def customer(self):
        if not hasattr(self._customer, 'resource'):
            self._item = Item._construct(obj=self._item)
        return self._customer

    def upgrade(self, item, currency='USD', **params):
        """ Upgrade a policy item.
        Keyword Arguments:
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
            billing_address (dict): The order's billing address. Required if
                                    card is given.
                                    Must include address1, address2, city,
                                    state, country, zip_code.

        Returns:
            An instance of the new policy that was created from upgrading. This
            object is updated to reflect the changes made.
        """
        card = params.get('card')
        if card:
            validate._validate_card(card)
            billing_address = params.get('billing_address')

            if not billing_address:
                raise NoBillingAddressException

            validate._validate_address(billing_address)

        upgrade = self.update(
            self.policy_number,
            'upgrade',
            item=item,
            currency=currency,
            raw_data=True,
            **params)

        # Since a few values change on the original policy this will update it
        self.status = UPGRADED

        # The new policy is returned.
        return Policy.retrieve(upgrade.get("policy_number"))
