from tg_sdk.abstract.list_resource import ListResourceMixin
from tg_sdk.abstract.retrieve_resource import RetrieveResourceMixin


class Affiliate(ListResourceMixin, RetrieveResourceMixin,):
    resource = "affiliates"
    id = None
    name = None
    domain = None
    _parent = None
    _settings = None

    @property
    def parent(self):
        if self._parent is None:
            return self.construct({})
        if not hasattr(self._parent, 'resource'):
            # TODO(Justin): This should construct an object and not make an
            #               API call. API calls should only be made when an
            #               attr of the parent is called.

            self._parent = self.retrieve(self._parent.id)
        return self._parent

    @property
    def settings(self):
        self.update(self._settings)
        return self._settings
