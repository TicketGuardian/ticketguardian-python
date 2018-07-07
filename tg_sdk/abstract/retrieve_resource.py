import json
import requests
from tg_sdk.api_resource import APIResource


class RetrieveResourceMixin(APIResource):

    @classmethod
    def retrieve(cls, resource_id, **params):
        """
        Retrieve a single resource and initialize an
        instance of the child object that called.
            Arguments:
                resource_id {str} -- The unique id of the resource.

            Keyword Arguments:
                public_key {str} -- The public key for this instance.
                secret_key {str} -- The secret key for this instance.
                env {str} -- The tg_sdk constant of the environment to use.
                             Billing and Core will be in the same env.
                             Prod will always be default.

            Returns:
                [object] -- An instance of the child object that called.
        """
        instance = cls()
        super(cls, instance).__init__(**params)
        url = "{}/api/v2/{}/{}/".format(
            instance.core_url,
            instance.resource,
            resource_id)

        response = requests.request(
            "GET",
            url,
            headers=instance.default_headers,
            params=params
        )

        if response.ok:
            data = json.loads(response.text)
        else:
            # TODO(Justin): ADD ERROR HANDLING
            return cls()

        return super(cls, instance).construct(data)

    def get_missing_attrs(instance):
        """
        Used to fill in any missing attributes in an object. List and Retrieve
        can return different attributes which so this makes another api call.
        """
        url = "{}/api/v2/{}/{}/".format(
            instance.core_url,
            instance.resource,
            instance.id)

        response = requests.request(
            "GET",
            url,
            headers=instance.default_headers,
        )

        if response.ok:
            data = json.loads(response.text)
            for attr in data:
                if not getattr(instance, '_' + attr, True):
                    instance.__setattr__('_' + attr, data[attr])

        else:
            # TODO(Justin): ADD ERROR HANDLING
            return None

    def update(self, val):
        """
        Used to fill in any missing attributes in an object. List and Retrieve
        can return different attributes which so this makes another api call.
            Arguments:
                val  -- The value the user is trying to get. This checks to
                        ensure that the object has already been updated and
                        the value is actually None.
        """
        if not self._updated and (self.id and val is None):
            self._updated = True
            self.get_missing_attrs()
