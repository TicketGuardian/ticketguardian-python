import os

from tg_sdk import constants

def affiliate_test_method(func):
    def wrapper():
        constants.PUBLIC_KEY = os.environ.get('AFF_PUB')
        constants.SECRET_KEY = os.environ.get('AFF_SEC')
        constants.ENV = 'dev'
    return wrapper

def client_test_method(func):
    def wrapper():
        constants.PUBLIC_KEY = os.environ.get('CLI_PUB')
        constants.SECRET_KEY = os.environ.get('CLI_SEC')
        constants.ENV = 'dev'
    return wrapper
