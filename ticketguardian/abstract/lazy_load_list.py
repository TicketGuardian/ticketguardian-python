from collections import defaultdict
from math import floor

from ticketguardian.constants import PAGE_SIZE


class LazyLoadMixin:
    def _update_list(self, offset, lazy=False):
        """
        Used to lazy load self._data when an page that has not been loaded
        is called.
        """
        obj_list = self._cls().get_list(
            offset=offset,
            *self._ext,
            **self._params)

        start_ind = offset
        end_ind = offset + len(obj_list)

        if lazy:
            start_ind = 0
            end_ind = PAGE_SIZE

        for i in range(start_ind, end_ind):
            self._data[i] = obj_list[i - start_ind]

    def _get_offset(self, ind):
        page_number = floor(ind / (PAGE_SIZE))
        return page_number * PAGE_SIZE


class ResourceList(list, LazyLoadMixin):
    def __init__(self, cls, size=None, data=None, slice_ind=0, *ext, **params):
        """
        cls: The class of the objects being listed
        size: The size of the ResourceList
              Defaults to count of resources and only used as a kwarg
              internally on sliced lists.
        data: A defaultdict containing the objects.
              Only used as a kwarg for sliced lists.
        slice_ind: Used to calculate the index of a sliced list since the same
                   data is used.
        ext: Strings that need to be added to the end of the URL.
        params: Extra params for the api call.
        """
        self._cls = cls
        self._size = size or self._cls().get_resource_count(*ext, **params)
        self._data = data or defaultdict(lambda: None)
        self._slice_ind = slice_ind
        self._ext = ext
        self._params = params

    def __repr__(self):
        return F"<{self._cls.__name__} ResourceList: {self._size} objects>"

    def __iter__(self):
        return ResourceIterator(
            cls=self._cls,
            size=self._size,
            data=self._data,
            slice_ind=self._slice_ind,
            *self._ext,
            **self._params
        )

    def __getitem__(self, ind):
        """
        Returns a new instance of ResourceList if a sliced list is needed.
        """
        if isinstance(ind, slice):
            start = ind.start or 0
            stop = ind.stop or self._size
            return ResourceList(
                cls=self._cls,
                size=stop - start,
                data=self._data,
                slice_ind=start,
                *self._ext,
                **self._params,
            )
        if ind >= self._size:
            raise IndexError('list index out of range')
        if ind < 0:
            # If index negative then get positive index
            ind += self._size
        else:
            # Add offsetting index
            ind += self._slice_ind

        if self._data[ind] is None:
            offset = self._get_offset(ind)
            self._update_list(offset)

        return self._data[ind]

    def __len__(self):
        return self._size

    def iterator(self):
        """
        Returns an iterator which only saves the current page in memory.
        """
        return ResourceIterator(
            cls=self._cls,
            size=self._size,
            data=self._data,
            slice_ind=self._slice_ind,
            lazy=True,
            *self._ext,
            **self._params
        )


class ResourceIterator(LazyLoadMixin):
    def __init__(self, cls, size, data, slice_ind=0, *ext, **params):
        """
        cls: The class of the objects being listed
        size: The size of the ResourceList
        data: A defaultdict containing the objects.
              Only used as a kwarg for sliced lists.
        offset: The first value on the current page.
        ind: The current index of the iterator.
        slice_ind: Used to calculate the index of a sliced list since the same
                   data is used.
        ext: Strings that need to be added to the end of the URL.
        params: Extra params for the api call.
        """
        self._cls = cls
        self._size = size
        self._data = data
        self._ind = 0
        self._slice_ind = slice_ind
        self._ext = ext
        self._params = params
        self._lazy = self._params.pop('lazy', False)

    def __iter__(self):
        return self

    def __next__(self):
        if self._ind < self._size:
            if self._data[self._index] is None:
                offset = self._get_offset(self._index)
                self._update_list(offset, self._lazy)

            obj = self._data[self._index]
            self._ind += 1
            return obj
        else:
            raise StopIteration

    @property
    def _index(self):
        ind = self._ind + self._slice_ind

        if self._lazy:
            ind = ind % PAGE_SIZE

        return ind
