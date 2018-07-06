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

# Configuration variables
PUBLIC_KEY = None
SECRET_KEY = None

# Constants
CORE_PROD = 'https://connect.ticketguardian.net'
CORE_DEV = "https://connect-dev.ticketguardian.net"
CORE_SANDBOX = 'https://connect-sandbox.ticketguardian.net'
BILLING_PROD = "https://billing.ticketguardian.net"
BILLING_DEV = "https://billing.ticketguardian.net"
BILLING_SANDBOX = "https://billing.ticketguardian.net"


from tg_sdk.product import Product
