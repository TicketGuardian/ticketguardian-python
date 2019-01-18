from ticketguardian._project._validate.exceptions import (
    InvalidCustomerInformationException, )

FIRST_NAME = "first_name"
LAST_NAME = "last_name"
EMAIL = "email"


def _validate_customer(customer):
    valid_info_set = {FIRST_NAME, LAST_NAME, EMAIL}
    customer_set = set(customer.keys())

    same_set = customer_set == valid_info_set
    if not valid_info_set.issubset(customer_set) and not same_set:
        raise InvalidCustomerInformationException
