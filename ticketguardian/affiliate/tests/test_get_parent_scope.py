from ticketguardian.affiliate import Affiliate


def test_get_parent_scope():
    affiliate = None
    for i in Affiliate.list():
        if i.parent is not None:
            # Get Affiliate that has a parent
            affiliate = i
            break

    parent = affiliate.parent
    parent_list = affiliate.get_parent_scope()

    for index, test_parent in enumerate(parent_list):
        assert parent.id == test_parent.id
        parent = parent.parent
