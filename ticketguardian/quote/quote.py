from ticketguardian.abstract import (
    PatchResourceMixin,
    PostResourceMixin,
)


class Quote(
    PostResourceMixin):
    resource = "quote"

    def __init__(self, currency='USD', **params):
        super().__init__()
        self.create(
            instance=self,
            items=params.get('items'),
            currency=currency)
