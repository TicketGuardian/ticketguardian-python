from tg_sdk.affiliate import Affiliate
from tg_sdk.client import Client
from tg_sdk.product import Product


class TicketGuardianSDK(object):
    def __init__(self, public_key, secret_key, env='prod'):
        self._public_key = public_key
        self._secret_key = secret_key
        self.env = env

    @property
    def _credentials(self):
        return {
            'public_key': self._public_key,
            'secret_key': self._secret_key,
            'env': self.env,
        }

    @property
    def Affiliate(self):
        return Affiliate(**self._credentials)

    @property
    def Client(self):
        return Client(**self._credentials)

    @property
    def Product(self):
        return Product(**self._credentials)
