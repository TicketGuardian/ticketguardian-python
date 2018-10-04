from tg_sdk.order.exceptions import InvalidShippingInformationException
ADDRESS1 = 'address1'
CITY = 'city'
STATE = 'state'
COUNTRY = 'country'
ZIPCODE = 'zip_code'

def _validate_address(address):
    required_fields = {ADDRESS1, CITY, STATE, COUNTRY, ZIPCODE}
    if not required_fields.issubset(set(address.keys())):
        raise InvalidShippingInformationException