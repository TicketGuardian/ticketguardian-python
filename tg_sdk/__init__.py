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

# Constants
BILLING_DEV = "https://billing-dev.ticketguardian.net"
BILLING_PROD = "https://billing.ticketguardian.net"
BILLING_SANDBOX = "https://billing-sandbox.ticketguardian.net"
CORE_DEV = "https://connect-dev.ticketguardian.net"
CORE_PROD = 'https://connect.ticketguardian.net'
CORE_SANDBOX = 'https://connect-sandbox.ticketguardian.net'

# Imports
from tg_sdk.ticketguardian_sdk import TicketGuardianSDK
from tg_sdk.affiliate import Affiliate
from tg_sdk.client import Client
from tg_sdk.product import Product
