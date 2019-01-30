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
                    assert resource_objects._data.get(j) is None
        ind += 1


@affiliate_test_method
def test_resourcelist_slice():
    # This tests that after each load the unloaded objects in the
    # list remain none.
    resource_objects = Policy.list()
    sliced = resource_objects[20:25]

    for ind, i in enumerate(sliced):
        # Assert that each value returned by the iterator is not None
        assert i is not None
        # Assert that the "parent" list resource_objects is updated with sliced
        assert resource_objects._data[ind + 20] == i
