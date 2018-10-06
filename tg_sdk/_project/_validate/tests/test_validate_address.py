import pytest

from tg_sdk._project._validate import _validate_address
from tg_sdk._project._validate.exceptions import (
    InvalidAddressInformationException, )


def test_validate_address_missing_field():
    params = {
        "city": "Woods Cross",
        "state": "UT",
        "zip_code": "84087",
        "country": "USA"
    }

    with pytest.raises(InvalidAddressInformationException):
        _validate_address(params)
