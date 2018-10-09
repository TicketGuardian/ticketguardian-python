from tg_sdk.abstract.validate.exceptions import (
    InvalidCardInformationException, )

NUMBER = 'number'
EXPIRE_MONTH = 'expire_month'
EXPIRE_YEAR = 'expire_year'


def _validate_card(card):
    valid_info_set = {NUMBER, EXPIRE_MONTH, EXPIRE_YEAR}
    card_set = set(card.keys())

    if not valid_info_set.issubset(card_set):
        raise InvalidCardInformationException