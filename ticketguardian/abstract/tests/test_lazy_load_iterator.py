from ticketguardian import Policy
from ticketguardian._project._decorators import affiliate_test_method


@affiliate_test_method
def test_lazy_iterator():
    # When using the iterator method in ResourceList only objects at index 0 to
    # 19 should be initialized
    resource_objects = Policy.list()
    ind = 0
    for i in resource_objects.iterator():
        if ind == 60:
            # Stop after 3 pages
            break

        if ind % 20 == 0:
            # Test each page for indexes 0 to 19
            for j in range(60):
                if j < 20:
                    assert resource_objects._data[j] is not None
                else:
                    assert resource_objects._data[j] is None
        ind += 1
