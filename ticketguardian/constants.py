# Constants
API_VERSION = 'api/v2'
BILLING_DEV = "https://billing-dev.ticketguardian.net"
BILLING_PROD = "https://billing.ticketguardian.net"
BILLING_SANDBOX = "https://billing-sandbox.ticketguardian.net"
CORE_DEV = "https://connect.ticketguardian-dev.net"
CORE_PROD = 'https://connect.ticketguardian.net'
CORE_SANDBOX = 'https://connect-sandbox.ticketguardian.net'
CORE_QA = 'https://connect.ticketguardian-qa.com'

DOMAINS = {
    "dev": {
        "core": CORE_DEV,
        "billing": BILLING_DEV
    },
    "sandbox": {
        "core": CORE_SANDBOX,
        "billing": BILLING_SANDBOX
    },
    "qa": {
        "core": CORE_QA
    },
    "prod": {
        "core": CORE_PROD,
        "billing": BILLING_PROD
    }
}

PUBLIC_KEY = ""
SECRET_KEY = ""
ENVIRONMENT = 'prod'
PAGE_SIZE = 20
