import math
import operator


class BaseHeap:

    def __init__(self):
        self.items = [None]

    def __iter__(self):
        while len(self.items) > 1:
            yield self.pop()

    def push(self, item):
        self.items.append(item)
        self._sift_up(len(self.items) - 1)

    def pop(self):
        if len(self.items) < 2:
            return None
        item = self.items[1]
        last_item = self.items.pop()
        if len(self.items) > 1:
            self.items[1] = last_item
            self._sift_down(1)
        return item

    def _sift_up(self, idx):
        while idx > 1:
            p_idx = math.floor(idx / 2)
            if self.gte(self.items[p_idx], self.items[idx]):
                break
            self.items[p_idx], self.items[idx] = self.items[idx], self.items[p_idx]
            idx = p_idx

    def _sift_down(self, idx):
        n = len(self.items)
        while True:
            l_idx = idx * 2
            l_child = self.items[l_idx] if l_idx < n else self.MIN
            r_idx = idx * 2 + 1
            r_child = self.items[r_idx] if r_idx < n else self.MIN

            if (self.gte(self.items[idx], l_child)
                and self.gte(self.items[idx], r_child)):
                break

            max_idx = l_idx if self.gte(l_child, r_child) else r_idx
            self.items[max_idx], self.items[idx] = self.items[idx], self.items[max_idx]
            idx = max_idx


class MinHeap(BaseHeap):
    MIN = float('inf')
    gte = operator.le


class MaxHeap(BaseHeap):
    MIN = float('-inf')
    gte = operator.ge


class InPlaceSortHeap:

    def __init__(self, items):
        self.count = len(items)
        self.items = items
        self._restore()
        self._sort()

    def _restore(self):
        for i in range(self.count // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sort(self):
        while self.count > 1:
            self._swap_items(0, self.count - 1)
            self.count -= 1
            self._sift_down(0)

    def _sift_down(self, i):
        while True:
            l_i = i * 2 + 1
            r_i = i * 2 + 2

            l_child = self.items[l_i] if l_i < self.count else None
            r_child = self.items[r_i] if r_i < self.count else None

            if ((not l_child or self.items[i] > l_child)
                and (not r_child or self.items[i] > r_child)):
                break

            max_i = l_i if (not r_child or l_child > r_child) else r_i
            self._swap_items(i, max_i)
            i = max_i

    def _swap_items(self, i1, i2):
        self.items[i1], self.items[i2] = self.items[i2], self.items[i1]
