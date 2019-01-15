# TicketGuardian Python Library
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2458/badge)](https://bestpractices.coreinfrastructure.org/projects/2458)
[![buddy pipeline](https://app.buddy.works/ticketguardian/ticketguardian-sdk/pipelines/pipeline/154249/badge.svg?token=a8d6086f0206fad0d2d5b576dd757c1d420553cdd3246f819b85fe21a1474c44 "buddy pipeline")](https://app.buddy.works/ticketguardian/ticketguardian-sdk/pipelines/pipeline/154249)

A python SDK for interacting with the TicketGuardian API


## Prerequisites

In order to use the TicketGuardian SDK, you must have a valid and active key pair.


## Installation

```
pip install git+https://github.com/TicketGuardian/ticketguardian-python
```


# Getting Started

The library needs to be configured to your active key pair. You can do that in one of two ways
### 1.
Set your `PUBLIC_KEY`, `SECRET_KEY`, and `ENVIRONMENT` within `credentials`.
```
# Enter a valid and active key pair

PUBLIC_KEY= ...
SECRET_KEY= ...
ENVIRONMENT= ...
```
### 2.
Set `PUBLIC_KEY` and `SECRET_KEY` to their appropriate values manually.
```
import tg_sdk
tg_sdk.PUBLIC_KEY = ...
tg_sdk.SECRET_KEY = ...
```

The default environment is `prod`, so if you would like to use another environment then set `tg_sdk.ENVIRONMENT` to the environment you would like to use.
`tg_sdk.ENVIRONMENT` only accepts `'prod'` or `'sandbox'`. Core and Billing will always use the same environment.

## Basic Usage

### Retrieving a Resource
```
from tg_sdk import Affiliate
aff1 = Affiliate.retrieve('af_123')
```

### Listing a Resource
```
# List of all objects
from tg_sdk import Affiliate
aff_list = Affiliate.list()

# List of filtered objects
from tg_sdk import Policy
policy_list = Policy.list(created__lte='2018-05-01T07:00:00')
```

# Advanced Usage

## Client
### Creating a Client
```
from tg_sdk import Client
Client.create(name='Client name', domain='client_domain.com', affiliate='af_123')
```

## Order
### Creating an Order
```
params = {
    "customer": {
        "first_name": "Richard",
        "last_name": "Hendricks",
        "email": "Rhendricks@piedpiper.com"
    },
    "order_number": 'ord_123',
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

## Adding Items to an Order
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

## Charge an Order
```
from tg_sdk import Order
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

order = Order.retrieve('ord_123')
order.charge(**params)
```


## Policy
### Upgrade Policy
```
params = {
    "currency": "EUR",
    "item": {
        "name": "Ticket 00001 - Johnny Appleseed",
        "reference_number": "ref_123",
        "cost": 100.00
    }
}

upgraded_policy = policy.upgrade(**params)
```

## Exchange Policy
```
params = {
    "item": {
        "name": "Ticket 00001 - Johnny Appleseed",
        "reference_number": "ref_123",
        "cost": 0.90
    },
    "currency": "USD",
}

policy.exchange(**params)
```

# Quote
```
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
