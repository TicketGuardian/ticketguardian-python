from tg_sdk.abstract import SDKException


class InvalidAddressInformationException(SDKException):
    message = "Shipping or Billing address must include Address1, "


class InvalidCardInformationException(SDKException):
    message = "Card must include `number`, `expire_month`, and `expire_year`"
