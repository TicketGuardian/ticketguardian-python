from ticketguardian.abstract import RetrieveResourceMixin


class Customer(RetrieveResourceMixin):
    resource = 'customers'
