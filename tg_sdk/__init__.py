"""
 _   _      _        _                            _ _
| |_(_) ___| | _____| |_ __ _ _   _  __ _ _ __ __| (_) __ _ _ __
| __| |/ __| |/ / _ \ __/ _` | | | |/ _` | '__/ _` | |/ _` | '_ \
| |_| | (__|   <  __/ || (_| | |_| | (_| | | | (_| | | (_| | | | |
 \__|_|\___|_|\_\___|\__\__, |\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|
                         |___/
"""


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

# Imports
from affiliate.affiliate import Affiliate
from client.client import Client
from constants import ENV, PUBLIC_KEY, SECRET_KEY
from customer.customer import Customer
from item.item import Item
from order.order import Order
from policy.policy import Policy
from product.product import Product
