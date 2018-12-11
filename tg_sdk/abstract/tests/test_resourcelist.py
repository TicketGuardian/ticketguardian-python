from tg_sdk._project._decorators import affiliate_test_method
from tg_sdk import Policy


@affiliate_test_method
def test_resourcelist_lazy_loads():
    # This tests that after each load the unloaded objects in the
    # list remain none.
    resource_objects = Policy.list()
    end = resource_objects._size if resource_objects._size < 60 else 60
    for i in range(0, end, 20):
        resource_objects[i]
        for j in range(0, end):
            if j <= i + 19:
                # if j < i + 19 then that page has been loaded so all should
                # not be None
                assert resource_objects._data[j] is not None
            else:
                # If j is greater than i then it should be None
                assert resource_objects._data[j] is None


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
