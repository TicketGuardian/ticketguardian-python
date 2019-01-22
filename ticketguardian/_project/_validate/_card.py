from ticketguardian._project._validate.exceptions import (
    InvalidCardInformationException, )

NUMBER = 'number'
EXPIRE_MONTH = 'expire_month'
EXPIRE_YEAR = 'expire_year'


def _validate_card(card):
    required_fields = {NUMBER, EXPIRE_MONTH, EXPIRE_YEAR}
    card_set = set(card.keys())

    same_set = required_fields == card_set
    if not required_fields.issubset(card_set) and not same_set:
        raise InvalidCardInformationException
