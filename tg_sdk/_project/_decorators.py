import os

import tg_sdk


def affiliate_test_method(func):
    def wrapper():
        tg_sdk.PUBLIC_KEY = os.environ.get('AFF_PUB')
        tg_sdk.SECRET_KEY = os.environ.get('AFF_SEC')
        tg_sdk.ENV = 'dev'
        func()
    return wrapper

def client_test_method(func):
    def wrapper():
        tg_sdk.PUBLIC_KEY = os.environ.get('CLI_PUB')
        tg_sdk.SECRET_KEY = os.environ.get('CLI_SEC')
        tg_sdk.ENV = 'dev'
        func()
    return wrapper
