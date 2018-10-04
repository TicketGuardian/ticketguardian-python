import tg_sdk


def test_exchange_policy():
    policy = tg_sdk.Policy.list(limit=1)[0]
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
    exchanged_item = policy.item
    updated_after = policy.updated

    for key in item:
        assert item.get(key) == getattr(exchanged_item, key)

    assert updated_before != updated_after
