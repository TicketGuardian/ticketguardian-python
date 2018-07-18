from datetime import datetime
import json
import requests

from tg_sdk import (
    BILLING_DEV,
    BILLING_PROD,
    BILLING_SANDBOX,
    CORE_DEV,
    CORE_PROD,
    CORE_SANDBOX, )
from tg_sdk.exceptions import (
    CouldNotRetrieveToken,
    CredentialsNotProvided, )


class APIResource(object):
    updated = False

    def __init__(self, **params):
        """
            Keyword Arguments:
                public_key (str) -- The public key for this instance.
                secret_key (str) -- The secret key for this instance.
                env (str) -- The tg_sdk constant of the environment to use.
                             Billing and Core will be in the same env.
                             Prod will always be default.
        """
        self._public_key = params.get('public_key', None)
        self._secret_key = params.get('secret_key', None)
        self._core_url = None
        self._billing_url = None
        self._env = params.get('env', 'prod')
        self.configure_environment(self._env)

    @classmethod
    def new_instance(cls, **params):
        return cls(**params)

    def construct(self, data):
        """
        Creates and initialized an instance of the child object that made
        the request. This checks first for the private variable to avoid
        recursive property calls. If the private variable does not exist then
        it is added as public.

            Arguments:
                data (dict) -- The dict containing the data for the object.

            Returns:
                object -- An instance of the child object.
        """
        instance = self.new_instance(**self.credentials)
        for key in data:
            if hasattr(instance, '_' + key):
                setattr(instance, '_' + key, data[key])
            else:
                setattr(instance, key, data[key])
        return instance

    def construct_general(self, name, data):
        """
        A generalized version of construct. This is used to create a type
        object that is initialized with the data from the dict.

            Returns:
                object -- An instance of the new object.
        """
        return type(name, (object,), data)

    def configure_environment(self, env):
        """
        Changes both billing and core url according to the string
        that is passed.

            Arguments:
                env (str) -- The name of the enviroment to change to.
                             Only accepts 'prod', 'dev', or 'sandbox'
        """
        env = env.lower()
        if env == 'dev':
            self._env = 'dev'
            self._core_url = CORE_DEV
            self._billing_url = BILLING_DEV
        elif env == 'sandbox':
            self._env = 'sandbox'
            self._core_url = CORE_SANDBOX
            self._billing_url = BILLING_SANDBOX
        elif env == 'prod':
            self._env = 'prod'
            self._core_url = CORE_PROD
            self._billing_url = BILLING_PROD
        else:
            # TODO(Justin): ADD ERROR HANDLING
            pass

    @property
    def credentials(self):
        return {
            'public_key': self._public_key,
            'secret_key': self._secret_key,
            'env': self._env,
        }

    @property
    def core_url(self):
        return self._core_url

    @property
    def billing_url(self):
        return self._billing_url

    def __setattr__(self, key, value):
        if hasattr(self, key) or key[0] == '_':
            return super().__setattr__(key, value)

    @property
    def token(self):
        if self.has_valid_token():
            return self._token
        elif self._public_key and self._secret_key:
            return self._refresh_token()
        else:
            raise CredentialsNotProvided

    @property
    def default_headers(self):
        return {
            'Accept': "application/json",
            'Content-Type': "application/json",
            'Authorization': "JWT " + self.token
        }

    @property
    def _token_payload(self):
        try:
            import jwt
            return jwt.decode(self._token, None, False)
        except Exception:
            return {}

    def has_valid_token(self):
        if not hasattr(self, '_token'):
            return False
        current_timestamp = datetime.now().timestamp()
        exp_timestamp = self._token_payload.get('exp', 0)
        return exp_timestamp > current_timestamp

    def _refresh_token(self):
        if not self._public_key and self._secret_key:
            raise CredentialsNotProvided(
                "Cannot refresh token without a valid public and secret key"
            )
        url = self.core_url + "/api/v2/auth/token/"
        payload = {
            "public_key": self._public_key,
            "secret_key": self._secret_key
        }
        headers = {
            'Accept': "application/json",
            'Content-Type': "application/json",
        }
        response = requests.request(
            "POST",
            url,
            data=json.dumps(payload),
            headers=headers
        )
        if response.ok:
            response_data = json.loads(response.text)
            if response_data.get("token"):
                self._token = response_data.get("token")
                return self._token
        raise CouldNotRetrieveToken(response.text)
