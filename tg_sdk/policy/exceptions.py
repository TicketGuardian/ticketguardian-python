from tg_sdk.abstract import SDKException


class NoBillingAddressException(SDKException):
    message = "You must provide a billing address"
