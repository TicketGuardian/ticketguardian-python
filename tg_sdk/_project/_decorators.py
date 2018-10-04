import os

from tg_sdk import constants

def affiliate_test_method(func):
    def wrapper():
        constants.AFF_PUB = os.environ.get('AFF_PUB')
        constants.AFF_SEC = os.environ.get('AFF_SEC')
        constants.ENV = 'dev'
    return wrapper

def client_test_method(func):
    def wrapper():
        constants.CLI_PUB = os.environ.get('CLI_PUB')
        constants.CLI_SEC = os.environ.get('CLI_SEC')
        constants.ENV = 'dev'
    return wrapper
