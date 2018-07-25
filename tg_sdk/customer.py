from tg_sdk.abstract.api_resource import APIResource


class Customer(APIResource,):
    # Todo(Justin): This is barebones for now just so I can have an object to
    #               return from other resource classes. I will add more
    #               functionality to this once I make more progress on those
    #               classes.
    id = None
    email = None
    first_name = None
    last_name = None
    phone = None
    shipping_address = None
    billing_address = None
