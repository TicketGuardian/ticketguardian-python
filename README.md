# TicketGuardian Python Library
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2458/badge)](https://bestpractices.coreinfrastructure.org/projects/2458)
[![buddy pipeline](https://app.buddy.works/ticketguardian/ticketguardian-sdk/pipelines/pipeline/154249/badge.svg?token=a8d6086f0206fad0d2d5b576dd757c1d420553cdd3246f819b85fe21a1474c44 "buddy pipeline")](https://app.buddy.works/ticketguardian/ticketguardian-sdk/pipelines/pipeline/154249)

A python SDK for interacting with the TicketGuardian API

## Documentation
* [API Documentation](https://docs.ticketguardian.net/)

## Prerequisites

In order to use the TicketGuardian SDK, you must have a valid and active key pair.

### Compatibilities
|              | Version       |
|:------------:|:-------------:|
| Python       |  3.6+         |

## Installation

```
pip install ticketguardian-python
```


# Getting Started

The library needs to be configured to your active key pair.
```
import ticketguardian
ticketguardian.PUBLIC_KEY = '...'
ticketguardian.SECRET_KEY = '...'
ticketguardian.ENVIRONMENT = 'sandbox'
```

If no environment is specified then `ticketguardian.ENVIRONMENT` defaults to `prod`.
`ticketguardian.ENVIRONMENT` only accepts `'prod'` or `'sandbox'`.

## Basic Usage

### Listing and Retrieving a Resource
```
# List of all objects
from ticketguardian import Affiliate
affiliate_list = Affiliate.list()

# List of filtered objects
from ticketguardian import Policy
policy_list = Policy.list(created__lte='2018-05-01T07:00:00')

# Retrieving a Resource
affiliate = affiliate_list[0]
affiliate_id = affiliate.id

same_affiliate = Affiliate.retrieve(affiliate_id)
```

## Advanced Usage

## Client
### Creating a Client
```
from ticketguardian import Client
Client.create(name='Client name', domain='client_domain.com', affiliate='af_123')
```

## Order
### Creating an Order
Note: Only Clients can create orders
```
from ticketguardian import Order
from random import choices
from string import ascii_uppercase

# Generate a unique order number
order_num = ''.join(choices(ascii_uppercase, k=55))

params = {
    "customer": {
        "first_name": "Richard",
        "last_name": "Hendricks",
        "email": "Rhendricks@piedpiper.com"
    },
    "order_number": order_num,
    "currency": "USD",
    "items": [
        {
            "name": "Name of item",
            "reference_number": 'ref_123',
            "cost": 10.00
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

order = Order.create(**params)
```
### Adding Items to an Order
```
params = {
    "currency": "USD",
    "items": [
        {
            "name": "Ticket 1 - New item",
            "reference_number": 'Ref_123',
            "cost": 90.00
        }
    ]
}

order.add_items(**params)
```
### Charge an Order
```
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

charge = order.charge(**params)
```


## Policy
### Upgrade Policy
```
from ticketguardian import Policy

params = {
    "currency": "EUR",
    "item": {
        "name": "Ticket 00001 - Johnny Appleseed",
        "reference_number": "ref_123",
        "cost": 100.00
    }
}

policy = Policy.list(status='Accepted')[0]
upgraded_policy = policy.upgrade(**params)
```

### Exchange Policy
```
from ticketguardian import Policy
params = {
    "item": {
        "name": "Ticket 00001 - Johnny Appleseed",
        "reference_number": "ref_123",
        "cost": 0.90
    },
    "currency": "USD",
}

policy = Policy.list(status='Issued')[0]
policy.exchange(**params)
```

# Quote
```
from ticketguardian import Quote

params = {
    "items": [
        {
            "name": "Ticket 00001 - Johnny Appleseed",
            "reference_number": "8M720WCMLO",
            "cost": "2000.00"
        },
        {
            "name": "Ticket 00002 - Tommy Appleseed",
            "reference_number": "8M720WCMLO",
            "cost": "30.00"
        }
    ],
    "currency": "CAD"
}

quote = Quote(**params)
```

# Testing Suite
To run the test suite first you need to enter a pair of active keys for an affiliate and a client in `.env`
```
AFF_PUB= '...'
AFF_SEC= '...'

CLI_PUB= '...'
CLI_SEC= '...'
```

Once the keys are set use the command `make tests` to start the testing suite.
