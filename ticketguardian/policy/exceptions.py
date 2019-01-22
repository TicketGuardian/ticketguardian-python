from ticketguardian.abstract import SDKException


class NoBillingAddressException(SDKException):
    message = "You must provide a billing address"
