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

    def __init__(self):
        super(User, self).__init__()
