from ticketguardian.abstract.sdk_exception import SDKException


class InvalidItemsException(SDKException):
    message = "`items` must be a list of item objects"


class InvalidCustomerInformationException(SDKException):
    message = "Customer must include 'first_name', 'last_name', and 'email'"
