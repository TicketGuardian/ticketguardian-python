from ticketguardian.abstract import APIResource, RetrieveResourceMixin


class Customer(RetrieveResourceMixin):
    resource = 'customers'

    def __init__(self):
        super(Customer, self).__init__()
