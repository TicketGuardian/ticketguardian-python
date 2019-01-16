import ticketguardian
from ticketguardian._project._decorators import client_test_method


@client_test_method
def test_exchange_policy():
    policy = ticketguardian.Policy.list(limit=1, status='Issued')[0]
    updated_before = policy.updated
    params = {
        "item": {
            "name": "Ticket 00004 - Johnny Appleseed",
            "reference_number": "{{$randomInt}}",
            "cost": "0.90"
        },
        "currency": "USD",
    }

    policy.exchange(**params)

    item = params.get('item')
    item['cost'] = float(item['cost'])
    exchanged_item = policy.item
    updated_after = policy.updated

    for key in item:
        assert item.get(key) == getattr(exchanged_item, key)

    assert updated_before != updated_after
