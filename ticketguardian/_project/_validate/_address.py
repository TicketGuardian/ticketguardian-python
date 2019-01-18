from ticketguardian._project._validate.exceptions import (
    InvalidAddressInformationException, )

ADDRESS1 = 'address1'
CITY = 'city'
STATE = 'state'
COUNTRY = 'country'
ZIPCODE = 'zip_code'


def _validate_address(address):
    required_fields = {ADDRESS1, CITY, STATE, COUNTRY, ZIPCODE}
    address_set = set(address.keys())

    if not required_fields.issubset(address_set) and \
       not address_set == required_fields:
        raise InvalidAddressInformationException
