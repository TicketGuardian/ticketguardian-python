from ticketguardian.abstract import (
    ListResourceMixin,
    PatchResourceMixin,
    PutResourceMixin,
    RetrieveResourceMixin, )


class User(
        ListResourceMixin,
        PatchResourceMixin,
        PutResourceMixin,
        RetrieveResourceMixin,):
    resource = "users"
