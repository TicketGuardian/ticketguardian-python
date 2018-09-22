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
    # c = tg.Client.create(**client_info)
    # TODO(Justin): I'm going to need to fix this. We can only use new names
    #               for clients so this fails since a client with this name
    #               is already archived
