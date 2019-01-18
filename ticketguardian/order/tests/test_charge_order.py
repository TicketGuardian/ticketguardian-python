from ticketguardian.order import Order
from ticketguardian._project._decorators import client_test_method


@client_test_method
def test_charge_order():
    params = {
        "policies": [
        ],
        "customer": {
            "first_name": "Galvin",
            "last_name": "Belson",
            "email": "g.Belson@hooli.com",
            "phone": "999-999-9999"
        },
        "billing_address": {
            "address1": "1 Hooli Dr",
            "city": "Newport Beach",
            "state": "CA",
            "zip_code": "92663",
            "country": "USA"
        },
        "card": {
            "number": "4111111111111111",
            "expire_month": "11",
            "expire_year": "20",
            "cvv": "123"
        }
    }
    order_limit = 100
    orders = Order.list(limit=order_limit)
    condition = True
    order = None

    while condition:
        """
        I am trying to find a better way to test this. I am doing this because
        I have to find an order that can be charged and I was having a hard
        time finding a simpler way.
        """
        for order in orders:
            for policy in order.policies:
                if policy.status == "Accepted":
                    condition = False
                    break
            if not condition:
                break
        order_limit += 100
        orders = Order.list(limit=order_limit)[order_limit - 100:]

    charge = order.charge(**params)

    charge_fields = {
        "msg": str,
        "policies": list,
        "is_success": bool,
        "exit": bool,
        "txn_id": str,
        "resource": str,
        "amount": str,
        "currency": str
    }

    for field in charge_fields:
        assert hasattr(charge, field)
        assert isinstance(getattr(charge, field), charge_fields[field])

    return charge
