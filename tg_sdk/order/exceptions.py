from tg_sdk.abstract.sdk_exception import SDKException


class InvalidItemsException(SDKException):
    message = "`items` must be a list of item objects"


class InvalidCardInformationException(SDKException):
    message = "Card must include `number`, `expire_month`, and `expire_year`"


class InvalidCustomerInformationException(SDKException):
    message = "Customer must include 'first_name', 'last_name', and 'email'"


class InvalidShippingInformationException(SDKException):
    message = "Shipping or Billing address must include Address1, "
