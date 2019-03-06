from ticketguardian.abstract import PostResourceMixin


class Quote(PostResourceMixin):
    resource = "quote"

    def __init__(self, currency='USD', **params):
        super(Quote, self).__init__()
        self.create(
            instance=self,
            items=params.get('items'),
            currency=currency)
