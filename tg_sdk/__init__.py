"""
 _   _      _        _                            _ _
| |_(_) ___| | _____| |_ __ _ _   _  __ _ _ __ __| (_) __ _ _ __
| __| |/ __| |/ / _ \ __/ _` | | | |/ _` | '__/ _` | |/ _` | '_ \
| |_| | (__|   <  __/ || (_| | |_| | (_| | | | (_| | | (_| | | | |
 \__|_|\___|_|\_\___|\__\__, |\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|
                         |___/
"""

# Imports
from tg_sdk.affiliate import Affiliate
from tg_sdk.client import Client
from tg_sdk import constants
from tg_sdk.customer import Customer
from tg_sdk.item import Item
from tg_sdk.order import Order
from tg_sdk.policy import Policy
from tg_sdk.product import Product
from tg_sdk.quote import Quote

# Credentials
import os
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
ENVIRONMENT = os.environ.get('ENVIRONMENT')

__title__ = 'TicketGuardian SDK'
__version__ = '0.0.0'
__author__ = 'TicketGuardian'
__license__ = 'GPLv3'
__copyright__ = 'Copyright 2017-2019 TicketGuardian'

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = 'iso-8859-1'

# Default datetime input and output formats
ISO_8601 = 'iso-8601'

__all__ = [
    "Affiliate",
    "Client",
    "constants",
    "Customer",
    "Item",
    "Order",
    "Policy",
    "Product",
    "Quote",
    "PUBLIC_KEY",
    "SECRET_KEY",
    "ENVIRONMENT",
]
