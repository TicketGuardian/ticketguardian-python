"""
 _   _      _        _                            _ _
| |_(_) ___| | _____| |_ __ _ _   _  __ _ _ __ __| (_) __ _ _ __
| __| |/ __| |/ / _ \ __/ _` | | | |/ _` | '__/ _` | |/ _` | '_ \
| |_| | (__|   <  __/ || (_| | |_| | (_| | | | (_| | | (_| | | | |
 \__|_|\___|_|\_\___|\__\__, |\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|
                         |___/
"""

# Imports
from .affiliate import Affiliate
from .client import Client
from .constants import ENV, PUBLIC_KEY, SECRET_KEY
from .customer import Customer
from .item import Item
from .order import Order
from .policy import Policy
from .product import Product

__title__ = 'TicketGuardian SDK'
__version__ = '0.0.0'
__author__ = 'TicketGuardian'
__license__ = 'BSD 3-Clause'
__copyright__ = 'Copyright 2017 TicketGuardian'

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = 'iso-8859-1'

# Default datetime input and output formats
ISO_8601 = 'iso-8601'

__all__ = [
    "Affiliate",
    "Client",
    "Customer",
    "ENV",
    "Item",
    "Order",
    "Policy",
    "Product",
    "PUBLIC_KEY",
    "SECRET_KEY",
]
