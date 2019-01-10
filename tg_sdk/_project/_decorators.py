import os

import tg_sdk


def affiliate_test_method(func):
    def wrapper():
        # Reading from environ for buddy tests
        pub = tg_sdk.constants.AFF_PUB or os.environ.get('AFF_PUB')
        sec = tg_sdk.constants.AFF_SEC or os.environ.get('AFF_SEC')
        tg_sdk.PUBLIC_KEY = pub
        tg_sdk.SECRET_KEY = sec
        tg_sdk.ENV = 'dev'
        func()
    return wrapper


def client_test_method(func):
    def wrapper():
        # Reading from environ for buddy tests
        pub = tg_sdk.constants.CLI_PUB or os.environ.get('CLI_PUB')
        sec = tg_sdk.constants.CLI_SEC or os.environ.get('CLI_SEC')
        tg_sdk.PUBLIC_KEY = pub
        tg_sdk.SECRET_KEY = sec
        tg_sdk.ENV = 'dev'
        func()
    return wrapper
