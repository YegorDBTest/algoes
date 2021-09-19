class BinarySearch:
    '''
    Binary search.

    Get first matched item index.

    Average complexity - O(log n).
    '''

    def __init__(self, data, item):
        '''
        data - sorted list.
        item - item to search in data.
        '''
        self._data = data
        self._item = item
        self._lower_index = 0
        self._higher_index = len(data) - 1
        self.index = self._get_index()

    def _get_index(self):
        while self._higher_index >= self._lower_index:
            half_index = self._get_half_index(self._lower_index, self._higher_index)
            if self._item == self._data[half_index]:
                return self._handle_equal(half_index)
            elif self._item > self._data[half_index]:
                self._handle_lower(half_index)
            else:
                self._handle_higher(half_index)
        return -1

    def _get_half_index(self, lower_index, higher_index):
        return lower_index + (higher_index - lower_index) // 2

    def _handle_equal(self, index):
        return index

    def _handle_lower(self, index):
        self._lower_index = index + 1

    def _handle_higher(self, index):
        self._higher_index = index - 1


class BinarySearchMin(BinarySearch):
    '''
    Min binary search.

    Find min matching item index if any, -1 otherwise.
    Additionaly find max index of item lower than matching item if any,
        -1 otherwise.

    Average complexity - O(log n).
    '''

    def __init__(self, data, item):
        '''
        data - sorted list.
        item - item to search in data.
        '''
        self.max_lower_index = -1
        super().__init__(data, item)

    def _handle_equal(self, index):
        while index - self.max_lower_index > 1:
            half_index = self._get_half_index(self.max_lower_index, index)
            if self._item == self._data[half_index]:
                index = half_index
            else:
                self.max_lower_index = half_index
        return index

    def _handle_lower(self, index):
        super()._handle_lower(index)
        self.max_lower_index = index


class BinarySearchMax(BinarySearch):
    '''
    Max binary search.

    Find max matching item index if any, -1 otherwise.
    Additionaly find min index of item higher than matching item if any,
        len(data) otherwise.

    Average complexity - O(log n).
    '''

    def __init__(self, data, item):
        '''
        data - sorted list.
        item - item to search in data.
        '''
        self.min_higher_index = len(data)
        super().__init__(data, item)

    def _handle_equal(self, index):
        while self.min_higher_index - index > 1:
            half_index = self._get_half_index(index, self.min_higher_index)
            if self._item == self._data[half_index]:
                index = half_index
            else:
                self.min_higher_index = half_index
        return index

    def _handle_higher(self, index):
        super()._handle_higher(index)
        self.min_higher_index = index
