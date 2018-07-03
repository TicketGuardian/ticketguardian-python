from tg_sdk.exceptions import CredentialsNotProvided, CouldNotRetrieveToken
from tg_sdk import token, public_key, secret_key, core_url, billing_url
from datetime import datetime
import requests
import json


class API_Resource(object):
    def __init__(self, **params):
        """
        Any value passed as a params will be prioritized over the configuration variables.
            Keyword Arguments:
                token {str} -- The Auth token for this instance.
                public_key {str} -- The public key for this instance.
                secret_key {str} -- The secret key for this instance.
                core_url {str} -- The url where requests will be made to.
                billing_url {str} -- The billing url where requests will be made to.
        """
        self._token = params.pop('token', token)
        self._public_key = params.pop('public_key', public_key)
        self._secret_key = params.pop('secret_key', secret_key)
        self._core_url = params.pop('core_url', core_url)
        self._billing_url = params.pop('billing_url', billing_url)

    def construct(instance, data):
        """
        Initializes an instance of the child class that made the request.
        If the object does not have an attr that is in the data then it is stored as a
        private variable.
            Arguments:
                data {dict} -- The dict of the item that was being searched for.
            Returns:
                [object] -- An instance of the child object.
        """
        for key in data:
            if hasattr(instance, key):
                instance.__setattr__(key, data[key])
            else:
                # if the object does not have the attr save as a private variable
                instance.__setattr__('_' + key, data[key])
        return instance

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
        if not (hasattr(self, '_public_key') and hasattr(self, '_secret_key')):
            raise CredentialsNotProvided(
                "Cannot refresh token without a valid public and secret key"
            )
        url = self._core_url + "/api/v2/auth/token/"
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
