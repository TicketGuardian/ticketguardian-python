from tg_sdk.abstract.api_resource import APIResource


class Policy(APIResource):
    # Todo(Justin): This is barebones for now just so I can have an object to
    #               return from other resource classes. I will add more
    #               functionality to this once I make more progress on those
    #               classes.
    created = None
    updated = None
    item = None
    customer = None
    policy_number = None
    premium = None
    coverage_amount = None
    currency = None
    status = None
