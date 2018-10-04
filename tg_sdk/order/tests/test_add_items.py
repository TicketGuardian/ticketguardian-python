from tg_sdk.order import Order
import tg_sdk
import random




def test_add_items_wo_card():
    tg_sdk.PUBLIC_KEY = tg_sdk.constants.CLI_PUB
    tg_sdk.SECRET_KEY = tg_sdk.constants.CLI_SEC
    tg_sdk.ENV = 'dev'

    order = Order.list(limit=1)[0]
    items_before = order.items
    params = {
        "currency": "USD",
        "items": [
          {
            "name": "Ticket 1 - AddItemTest ABC 123",
            "reference_number": "reference_num_" + str(random.randint(1, 10)),
            "cost": 90.00
          }
        ]
    }
    order.add_items(**params)
    assert len(order.items) == len(items_before) + 1

    new_item = order.items[0]
    for key in params['items'][0]:
        assert getattr(new_item, key) == params['items'][0][key]


def test_add_items_w_card():
    tg_sdk.PUBLIC_KEY = tg_sdk.constants.CLI_PUB
    tg_sdk.SECRET_KEY = tg_sdk.constants.CLI_SEC
    tg_sdk.ENV = 'dev'

    order = Order.list(limit=1)[0]
    items_before = order.items
    params = {
        "card": {
            "number": "4111111111111111",
            "expire_month": "11",
            "expire_year": "20",
        },
        "currency": "USD",
        "items": [
          {
            "name": "Ticket 1 - AddItemTest ABC 123",
            "reference_number": "reference_num_" + str(random.randint(1, 10)),
            "cost": 90.00
          }
        ]
    }
    order.add_items(**params)
    assert len(order.items) == len(items_before) + 1

    new_item = order.items[0]
    for key in params['items'][0]:
        assert getattr(new_item, key) == params['items'][0][key]

def test_add_multiple_items():
    tg_sdk.PUBLIC_KEY = tg_sdk.constants.CLI_PUB
    tg_sdk.SECRET_KEY = tg_sdk.constants.CLI_SEC
    tg_sdk.ENV = 'dev'

    order = Order.list(limit=1)[0]
    items_before = order.items
    params = {
        "currency": "USD",
        "items": [
            {
                "name": "Ticket 1 - AddItemTest ABC 123",
                "reference_number": "reference_num_" + str(
                    random.randint(1, 10)),
                "cost": 90.00
            },
            {
                "name": "Ticket 2 - AddItemTest ABC 123",
                "reference_number": "reference_num_" + str(
                    random.randint(1, 10)),
                "cost": 9.00
            },
            {
                "name": "Ticket 3 - AddItemTest ABC 123",
                "reference_number": "reference_num_" + str(
                    random.randint(1, 10)),
                "cost": 10.00
            }
        ]
    }
    order.add_items(**params)
    assert len(order.items) == len(items_before) + 3

    new_items = order.items[0:3]
    for ind, item in enumerate(params['items']):
        new_item = new_items[2-ind]
        for key in item:
            assert getattr(new_item, key) == item[key]
