import tg_sdk


def affiliate_test_method(func):
    def wrapper():
        tg_sdk.PUBLIC_KEY = tg_sdk.constants.AFF_PUB
        tg_sdk.SECRET_KEY = tg_sdk.constants.AFF_SEC
        tg_sdk.ENV = 'dev'
        func()
    return wrapper


def client_test_method(func):
    def wrapper():
        tg_sdk.PUBLIC_KEY = tg_sdk.constants.CLI_PUB
        tg_sdk.SECRET_KEY = tg_sdk.constants.CLI_SEC
        tg_sdk.ENV = 'dev'
        func()
    return wrapper
