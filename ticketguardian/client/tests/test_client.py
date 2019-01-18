from ticketguardian._project._decorators import affiliate_test_method


@affiliate_test_method
def test_client_post():
    client_info = {
        'name': 'PostMixinTest',
        'domain': 'PostMixinTest.net',
        'affiliate': 'af_xgFkJRVh'
    }
    return client_info
