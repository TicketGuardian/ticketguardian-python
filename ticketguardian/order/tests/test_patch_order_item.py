from ticketguardian.order import Order


def test_order_item_patch():
    order = Order.list(limit=1)[0]
    order.patch(attrs='test_patch')
    assert order.attrs == 'test_patch'
