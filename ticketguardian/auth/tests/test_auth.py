from ticketguardian.affiliate import Affiliate
from ticketguardian.auth import Auth
from ticketguardian.client import Client

from ticketguardian._project._decorators import affiliate_test_method


@affiliate_test_method
def test_auth_get_scope_affiliate():
    affiliate = Affiliate.list()[0]
    scope = Auth.get_scope(root_type='affiliate', root_id=affiliate.id)

    # assert format
    assert isinstance(scope, list)
    assert isinstance(scope[0], list)
    assert isinstance(scope[0][0], str)


@affiliate_test_method
def test_auth_get_scope_client():
    client = Client.list()[0]
    scope = Auth.get_scope(root_type='client', root_id=client.id)

    # assert format
    assert isinstance(scope, list)
    assert isinstance(scope[0], list)
    assert isinstance(scope[0][0], str)


@affiliate_test_method
def test_auth_get_my_scope():
    scope = Auth.get_scope()

    # assert format
    assert isinstance(scope, list)
    assert isinstance(scope[0], list)
    assert isinstance(scope[0][0], str)


@affiliate_test_method
def test_auth_get_me():
    me = Auth.me()
    assert isinstance(me.get('id'), str)
