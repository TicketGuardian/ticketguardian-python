from ticketguardian.affiliate import Affiliate
from ticketguardian.auth import Auth
from ticketguardian.client import Client

from ticketguardian._project._decorators import affiliate_test_method


@affiliate_test_method
def test_auth_get_my_scope():
    scope = Auth().get_scope()

    # assert format
    assert isinstance(scope, list)
    assert isinstance(scope[0], list)
