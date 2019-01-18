from ticketguardian.abstract import SDKException


class InvalidAddressInformationException(SDKException):
    message = "Shipping or Billing address must include Address1, \
               city, state, country, and zip_code"


class InvalidCardInformationException(SDKException):
    message = "Card must include `number`, `expire_month`, and `expire_year`"


class InvalidCustomerInformationException(SDKException):
    message = "Customer must include first_name, last_name, email, and phone"
