import os

import ticketguardian


def affiliate_test_method(func):
    def wrapper():
        ticketguardian.PUBLIC_KEY = os.environ.get('AFF_PUB')
        ticketguardian.SECRET_KEY = os.environ.get('AFF_SEC')
        ticketguardian.ENVIRONMENT = 'dev'
        func()
    return wrapper


def client_test_method(func):
    def wrapper():
        ticketguardian.PUBLIC_KEY = os.environ.get('CLI_PUB')
        ticketguardian.SECRET_KEY = os.environ.get('CLI_SEC')
        ticketguardian.ENVIRONMENT = 'dev'
        func()
    return wrapper
