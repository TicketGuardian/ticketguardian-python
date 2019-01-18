import random
import uuid

from ticketguardian.order import Order
from ticketguardian._project._decorators import client_test_method


@client_test_method
def test_create_order_wo_card():
    params = {
        "customer": {
            "first_name": "SDK",
            "last_name": "TEST",
            "email": "SDK@ticketguardian.net"
        },
        "order_number": str(uuid.uuid4()),
        "currency": "USD",
        "items": [
            {
                "name": "Test VIP",
                "reference_number": "BI-VIP" + str(uuid.uuid4())[:5],
                "cost": str(round(random.uniform(1, 100), 2))
            }
        ],
        "billing_address": {
            "address1": "123 Oregon way",
            "address2": "apt",
            "city": "Salt Lake City",
            "state": "UT",
            "country": "US",
            "zip_code": "84101"
        }
    }

    order = Order.create(**params)
    params.pop('billing_address')

    for key in params:
        assert hasattr(order, key)

    assert hasattr(order.customer, 'billing_address')


@client_test_method
def test_create_order_w_card():
    params = {
        "customer": {
            "first_name": "SDK",
            "last_name": "TEST w/ card",
            "email": "SDK@ticketguardian.net"
        },
        "card": {
            "number": "4111111111111111",
            "expire_month": "11",
            "cvv": 123,
            "expire_year": "20"
        },
        "order_number": str(uuid.uuid4()),
        "currency": "USD",
        "items": [
            {
                "name": "Test VIP",
                "reference_number": "BI-VIP" + str(uuid.uuid4())[:5],
                "cost": str(round(random.uniform(1, 100), 2))
            }
        ],
        "billing_address": {
            "address1": "123 Oregon way",
            "address2": "apt",
            "city": "Salt Lake City",
            "state": "UT",
            "country": "US",
            "zip_code": "84101"
        }
    }

    order = Order.create(**params)
    params.pop('billing_address')
    params.pop('card')

    for key in params:
        assert hasattr(order, key)

    assert hasattr(order.customer, 'billing_address')
