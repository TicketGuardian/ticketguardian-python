import pytest

from tg_sdk._project._validate import _validate_card
from tg_sdk._project._validate.exceptions import (
    InvalidCardInformationException, )


def test_validate_card():
    params = {
        "expire_month": "11",
        "expire_year": "20",
        "cvv": "123"
    }

    with pytest.raises(InvalidCardInformationException):
        _validate_card(params)