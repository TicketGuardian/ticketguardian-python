from ticketguardian._project._decorators import affiliate_test_method
from ticketguardian import Policy


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
