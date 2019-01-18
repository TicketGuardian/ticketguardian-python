"""
 _   _      _        _                            _ _
| |_(_) ___| | _____| |_ __ _ _   _  __ _ _ __ __| (_) __ _ _ __
| __| |/ __| |/ / _ \ __/ _` | | | |/ _` | '__/ _` | |/ _` | '_ \
| |_| | (__|   <  __/ || (_| | |_| | (_| | | | (_| | | (_| | | | |
 \__|_|\___|_|\_\___|\__\__, |\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|
                         |___/
"""

# Imports
from ticketguardian.affiliate import Affiliate
from ticketguardian.client import Client
from ticketguardian import constants
from ticketguardian.customer import Customer
from ticketguardian.item import Item
from ticketguardian.order import Order
from ticketguardian.policy import Policy
from ticketguardian.product import Product
from ticketguardian.quote import Quote

# Credentials
import os
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
ENVIRONMENT = os.environ.get('ENVIRONMENT')

__title__ = 'TicketGuardian SDK'
__author__ = 'TicketGuardian'
__license__ = 'GPLv3'
__copyright__ = 'Copyright 2017-2019 TicketGuardian'


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
