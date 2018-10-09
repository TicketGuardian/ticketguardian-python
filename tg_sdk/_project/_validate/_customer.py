from tg_sdk._project._validate.exceptions import (
    InvalidCustomerInformationException, )

FIRST_NAME = "first_name"
LAST_NAME = "last_name"
EMAIL = "email"


def _validate_customer(customer):
    valid_info_set = {FIRST_NAME, LAST_NAME, EMAIL}
    customer_set = set(customer.keys())

    if not valid_info_set.issubset(customer_set) and \
    not customer_set == valid_info_set:
        raise InvalidCustomerInformationException
