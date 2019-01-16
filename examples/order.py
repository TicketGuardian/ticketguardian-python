import ticketguardian
from random import choices
from string import ascii_uppercase

# Authenticate as a Client to use this example
ticketguardian.PUBLIC_KEY = ''
ticketguardian.SECRET_KEY = ''
ticketguardian.ENVIRONMENT = 'sandbox'

# Generate a unique order number
order_num = ''.join(choices(ascii_uppercase, k=55))

order_params = {
    "customer": {
        "first_name": "Richard",
        "last_name": "Hendricks",
        "email": "Rhendricks@piedpiper.com"
    },
    "order_number": order_num,
    "currency": "USD",
    "items": [
        {
            "name": "Pied Piper Con GA Pass",
            "reference_number": 'ref_123',
            "cost": 500.00
        },
        {
            "name": "Pied Piper Con Half Day Pass",
            "reference_number": 'ref_123',
            "cost": 100.00
        }
    ],
    "billing_address": {
        "address1": "123 Memory Ln",
        "address2": "APT 1",
        "city": "Salt Lake City",
        "state": "UT",
        "country": "US",
        "zip_code": "84101"
    }
}

# Get a quote for the order
# Note: Quote uses USD as its default currency
order_quote = ticketguardian.Quote(items=order_params['items'])

# Data returned from Quote()
quote_data = {
    'currency': order_quote.currency,
    'symbol': order_quote.symbol,
    'total': order_quote.total,
    'quote': order_quote.quote
}

# Create the order
order = ticketguardian.Order.create(**order_params)

order_data = {
    'created': order.created,
    'updated': order.updated,
    'order_number': order.order_number,
    'subtotal': order.subtotal,
    'currency': order.currency,
    'client': order.client,
    'items': order.items,
    'id': order.id,
    'policies': order.policies,
    'customer': order.customer
}

# Charge the order
charge_params = {
    "policies": [policy.policy_number for policy in order.policies],
    "customer": {
        "first_name": order.customer.first_name,
        "last_name": order.customer.last_name,
        "email": order.customer.email,
        "phone": order.customer.phone
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

charge = order.charge(**charge_params)

charge_data = {
    'msg': charge.msg,
    'policies': charge.policies,
    'is_success': charge.is_success,
    'exit': charge.exit,
    'txd_if': charge.txn_id,
    'resource': charge.resource,
    'amount': charge.amount,
    'currency': charge.currency
}
