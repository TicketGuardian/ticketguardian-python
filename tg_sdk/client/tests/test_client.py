import tg_sdk

tg_sdk.PUBLIC_KEY = tg_sdk.AFF_PUB
tg_sdk.SECRET_KEY = tg_sdk.AFF_SEC
tg_sdk.ENV = 'DEV'


def test_client_post():
    client_info = {
        'name': 'PostMixinTest',
        'domain': 'PostMixinTest.net',
        'affiliate': 'af_xgFkJRVh'
    }
    return client_info
    # c = tg.Client.create(**client_info)
