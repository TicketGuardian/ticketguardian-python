from tg_sdk.abstract.sdk_exception import SDKException


class InvalidItemsException(SDKException):
    message = "`items` must be a list of item objects"


class InvalidCardInformationException(SDKException):
    message = "Card must include `number`, `expire_month`, and `expire_year`"
