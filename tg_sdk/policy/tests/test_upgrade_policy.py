import pytest

import tg_sdk
from tg_sdk.policy.exceptions import NoBillingAddressException


def test_upgrade_policy_wo_card():
    tg_sdk.PUBLIC_KEY = tg_sdk.constants.CLI_PUB
    tg_sdk.SECRET_KEY = tg_sdk.constants.CLI_SEC
    tg_sdk.ENV = 'dev'

    policy = tg_sdk.Policy.list(limit=1, status='Accepted')[0]

    params = {
        "currency": "EUR",
        "item": {
            "name": "Ticket 00004 - Johnny Appleseed",
            "reference_number": "{{$randomInt}}",
            "cost": "100.00"
        }
    }

    upgraded_policy = policy.upgrade(**params)

    item = params.get('item')
    item['cost'] = float(item['cost'])
    upgraded_item = upgraded_policy.item
    for key in item:
        assert item.get(key) == getattr(upgraded_item, key)

    assert policy.status == tg_sdk.policy.constants.UPGRADED


def test_upgrade_policy_w_card():
    policy = tg_sdk.Policy.list(limit=1, status='Accepted')[0]

    params = {
        "billing_address": {
            "address1": "1174 West 1700 South",
            "city": "Woods Cross",
            "state": "UT",
            "zip_code": "84087",
            "country": "USA"
        },
        "card": {
            "number": "4111111111111111",
            "expire_month": "11",
            "expire_year": "20",
            "cvv": "123"
        },
        "currency": "USD",
        "item": {
            "name": "Ticket 00004 - Johnny Appleseed",
            "reference_number": "125416",
            "cost": "900.00"
        }
    }

    upgraded_policy = policy.upgrade(**params)

    item = params.get('item')
    item['cost'] = float(item['cost'])
    upgraded_item = upgraded_policy.item
    for key in item:
        assert item.get(key) == getattr(upgraded_item, key)

    assert policy.status == tg_sdk.policy.constants.UPGRADED


def test_cannot_upgrade_w_card_wo_billing_address():
    policy = tg_sdk.Policy.list(limit=1, status='Accepted')[0]

    params = {
        "card": {
            "number": "4111111111111111",
            "expire_month": "11",
            "expire_year": "20",
            "cvv": "123"
        },
        "currency": "USD",
        "item": {
            "name": "Ticket 00004 - Johnny Appleseed",
            "reference_number": "125416",
            "cost": "900.00"
        }
    }

    with pytest.raises(NoBillingAddressException):
        policy.upgrade(**params)
