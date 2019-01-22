from datetime import datetime
import json
import requests

from ticketguardian.constants import (
    API_VERSION,
    BILLING_DEV,
    BILLING_PROD,
    BILLING_SANDBOX,
    CORE_DEV,
    CORE_PROD,
    CORE_SANDBOX,)
from ticketguardian.exceptions import (
    CouldNotRetrieveToken,
    CredentialsNotProvided, )


class APIResource(object):
    is_updated = False

    def __init__(self, **params):
        """
        Keyword Arguments:
            public_key (str) -- The public key for this instance.
            secret_key (str) -- The secret key for this instance.
            env (str) -- The environment where requests will be made.
                         Billing and Core will be in the same env.
                         Prod will always be default.
                         input can only be 'prod' or 'sandbox'
        """
        from ticketguardian import PUBLIC_KEY, SECRET_KEY, ENVIRONMENT
        self._public_key = params.get('public_key', PUBLIC_KEY)
        self._secret_key = params.get('secret_key', SECRET_KEY)
        self._core_url = None
        self._billing_url = None
        self._token = None
        self._env = params.get('env', ENVIRONMENT)
        self._configure_environment(self._env)

    def __setattr__(self, key, value):
        if isinstance(value, dict):
            value = self._construct_general(key.title(), value)

        if key in vars(type(self)):
            return super().__setattr__('_' + key, value)
        else:
            return super().__setattr__(key, value)

    def __repr__(self):
        resource_name = self.__class__.__name__
        if hasattr(self, 'id'):
            return F'<{resource_name.title()}: {self.id}>'
        else:
            return F'<{resource_name.title()} object at {hex(id(self))}>'

    @classmethod
    def _construct(cls, **params):
        """
        Creates an instance of the child object that made the request.
        This checks first for the private variable to avoid recursive property
        calls. If the private variable does not exist then it is added as
        public.
            Keyword Arguments:
                obj -- A type object to iterate through for data.
            Returns:
                object -- An instance of the child object.
        """
        instance = params.pop('instance', None)
        if not instance:
            instance = cls()
        if 'obj' in params:
            data = params.pop('obj').__dict__
            for key in data:
                if key[0] != '_':
                    params[key] = data[key]

        for key in params:
            setattr(instance, key, params.get(key))
        return instance

    def _construct_general(self, name, data):
        """
        A generalized version of construct. This is used to create a type
        object that is initialized with the data from the dict.
        This method differs from construct by only creating a type object with
        data from a dict rather than initializing an instance for a resource
        object.
            Arguments:
                name (str) -- The name of the object that is going to be
                              constructed.
                data (dict) -- The dict containing the data to be stored.

            Returns:
                object -- An instance of the new object.
        """
        return type(name, (object,), data)

    def _construct_list(self, li, cls):
        """
        Takes a list of dictionaries and makes each dict in the list into the
        given object type.
            Arguments:
                li (list) -- The list of dictionaries.
                cls (object) -- The object type to create.
            Returns:
                A list of objects of the given object type.
        """
        return [cls._construct(**data) for data in li]

    def _configure_environment(self, env):
        """
        Changes both billing and core url according to the string that is
        passed.

            Arguments:
                env (str) -- The name of the environment to change to.
                             Only accepts 'prod' or 'sandbox'
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
            raise Exception("Invalid environment. "
                            "Use prod' or 'sandbox'")

    def _make_url(self, *args):
        """
        Used internally to make urls for the mixins.
        Arguments:
            Any extension of the url as strings. The default url is the
            {core url}/{api version}/{resource name}
        """
        url = "{}/{}/{}/".format(
            self.core_url,
            API_VERSION,
            self.resource
        )
        for arg in args:
            url += "{}/".format(arg)
        return url

    @property
    def _get_object_id(self):
        """
        Used in the few cases that an objects id is not named id
            For example, Items have an id attribute but Orders have an
            order-number
        :return: The id of the object
        """
        if hasattr(self, 'id_name'):
            return getattr(self, self.id_name)
        return self.id

    @property
    def core_url(self):
        return self._core_url

    @property
    def billing_url(self):
        return self._billing_url

    @property
    def token(self):
        if self._has_valid_token():
            return self._token
        elif self._public_key and self._secret_key:
            return self._refresh_token()
        else:
            raise CredentialsNotProvided

    @property
    def _default_headers(self):
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

    def _has_valid_token(self):
        if self._token is None:
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
