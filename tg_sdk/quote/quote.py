from tg_sdk.abstract import PostResourceMixin


class Quote(PostResourceMixin):
    resource = "quote"

    def __init__(self, items, currency='USD'):
        super().__init__()
        self.create(instance=self, items=items, currency=currency)
