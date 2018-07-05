import requests
import json
from datetime import datetime
from tg_sdk.exceptions import CredentialsNotProvided, CouldNotRetrieveToken
from tg_sdk import PUBLIC_KEY, SECRET_KEY, CORE_URL, BILLING_URL


class APIResource(object):
    def __init__(self, **params):
        """
        Any value passed in params will be prioritized over the configuration variables.
            Keyword Arguments:
                public_key {str} -- The public key for this instance.
                secret_key {str} -- The secret key for this instance.
                environment {str} -- The name of the environment that requests will be made to.
                billing_url {str} -- The billing url where requests will be made to.
        """
        self._public_key = params.pop('public_key', PUBLIC_KEY)
        self._secret_key = params.pop('secret_key', SECRET_KEY)
        self._environment = params.pop('environment', 'prod')
        self._billing_url = params.pop('billing_url', BILLING_URL)

    def construct(instance, data):
        """
        Initializes an instance of the child object that made the request.
        If the object does not have an attr that is in the data then it is stored as a
        private variable.
            Arguments:
                instance {object} -- The new instance of the object to initialize.
                data {dict} -- The dict of the item that was being searched for.
            Returns:
                [object] -- An instance of the child object.
        """
        for key in data:
            if hasattr(instance, key):
                instance.__setattr__(key, data[key])
            else:
                instance.__setattr__('_' + key, data[key])
        return instance

    @property
    def core_url(self):
        """
        This will always default to prod if no environment or an invalid environment is given.
            Returns:
                [str] -- the url of the environments where requests will be made.
        """
        if self._environment.lower() == 'sandbox':
            return 'https://connect-sandbox.ticketguardian.net'
        else:
            return 'https://connect.ticketguardian.net'

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
