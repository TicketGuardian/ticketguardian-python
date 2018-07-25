# Python Client for TicketGuardian API

A python SDK for interacting with the TicketGuardian API

## Getting Started


### Prerequisites

In order to use the TicketGuardian SDK, you must have a valid and active key pair.


## Installation

```
pip install git+https://github.com/TicketGuardian/ticketguardian-python
```


## Usage

The library needs to be configured to your active key pair. Set `tg_sdk.PUBLIC_KEY` and `tg_sdk.SECRET_KEY` to their appropriate values:
```
import tg_sdk
tg_sdk.PUBLIC_KEY = ...
tg_sdk.SECRET_KEY = ...
```

The default environment is prod, so if you would like to use another environment then set `tg_sdk.ENV` to the environment you would like to use.
`tg_sdk.ENV` only accepts 3 strings `'prod'`, `'dev'`, or `'sandbox'`. Core and Billing will always use the same environment.
```
tg_sdk.ENV = 'dev'
```

```
# Initialize SDK
import tg_sdk
tg_sdk.PUBLIC_KEY = ...
tg_sdk.SECRET_KEY = ...

# Set Environment
# NOTE: tg_sdk.ENV can only be 'prod', 'dev', or 'sandbox'.
#       'prod' will always be default is no ENV is provided.
tg_sdk.ENV = 'dev'

# Retrieving a single resource
affiliate1 = tg_sdk.Affiliate.retrieve('uniqueid')

# Listing out resources
all_affiliates = tg_sdk.Affiliate.list()
filtered_affiliates = tg_sdk.Affiliate.list(filter1=..., filter2=...)
max10_affiliates = tg_sdk.Affiliates.list(limit=10)

# Posting a new resource
new_client = tg_sdk.Client.post(attr1=..., attr2=...)

# Updating a resource
order = tg_sdk.Order.retrieve(...)
order.add_items(arg1=..., arg2=...)
```
