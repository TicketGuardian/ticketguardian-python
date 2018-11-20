from math import ceil

PAGE_SIZE = 20


class LazyLoadMixin:
    def _update_list(self, offset):
        """
        Used to lazy load self._data when an page that has not been loaded
        is called. This will make an API request to get a list of objects
        with the size PAGE_SIZE or size of remaining spots in list.
        """
        limit = None
        if offset + PAGE_SIZE > self._size:
            # If the index at the end of the page is larger than
            # the size of the list then we need the number of spaces
            # left to fill
            limit = PAGE_SIZE - ((offset + PAGE_SIZE) - self._size)

        obj_list = self._cls().get_list(offset=offset, limit=limit)

        start_ind = offset
        end_ind = offset + PAGE_SIZE

        if limit:
            end_ind = self._size

        self._data[start_ind:end_ind] = obj_list


class Resource_List(list, LazyLoadMixin):
    def __init__(self, cls, size=None):
        self._cls = cls
        self._size = size or self._cls().get_resource_count()
        self._data = [None] * self._size

    def __repr__(self):
        return str(self._data)

    def __iter__(self):
        return Resource_Iterator(
            cls=self._cls,
            size=self._size,
            data=self._data
        )

    def __getitem__(self, ind):
        temp = ind
        if self._data[ind] is None:
            if ind == 0:
                # Add 1 to avoid negative offset
                temp += 1
            if ind < 0:
                temp += self._size

            multiple = ceil(temp / PAGE_SIZE) - 1
            offset = multiple * PAGE_SIZE
            self._update_list(offset)

        return self._data[ind]

    def __len__(self):
        return len(self._data)


class Resource_Iterator(LazyLoadMixin):
    def __init__(self, cls, size, data, *args, **params):
        self._cls = cls
        self._size = size
        self._data = data
        self._offset = 0
        self._index = 0

    def __next__(self):
        if self._index < self._size:
            if self._data[self._index] is None:
                self._update_list(self._offset)
                self._offset += 20

            obj = self._data[self._index]
            self._index += 1
            return obj
        else:
            raise StopIteration
