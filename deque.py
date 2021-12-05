class InvalidDequeOperation(Exception):
    pass


class LimitSizeDeque:

    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = max_size - 1
        self.size = 0

    @property
    def is_push_valid(self):
        return self.size < self.max_size

    @property
    def is_pop_valid(self):
        return self.size > 0

    def push_back(self, item):
        if not self.is_push_valid:
            raise InvalidDequeOperation
        self.tail = self._increase_index(self.tail)
        self.items[self.tail] = item
        self.size += 1

    def push_front(self, item):
        if not self.is_push_valid:
            raise InvalidDequeOperation
        self.head = self._decrease_index(self.head)
        self.items[self.head] = item
        self.size += 1

    def pop_back(self):
        if not self.is_pop_valid:
            raise InvalidDequeOperation
        item = self.items[self.tail]
        self.items[self.tail] = None
        self.tail = self._decrease_index(self.tail)
        self.size -= 1
        return item

    def pop_front(self):
        if not self.is_pop_valid:
            raise InvalidDequeOperation
        item = self.items[self.head]
        self.items[self.head] = None
        self.head = self._increase_index(self.head)
        self.size -= 1
        return item

    def _increase_index(self, index):
        return (index + 1) % self.max_size

    def _decrease_index(self, index):
        return (index - 1 + self.max_size) % self.max_size
