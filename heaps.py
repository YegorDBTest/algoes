import math
import operator


class BaseHeap:

    def __init__(self):
        self.items = [None]

    def add_item(self, item):
        self.items.append(item)
        self._sift_up(len(self.items))

    def extract_item(self, idx):
        n = len(self.items)
        if idx >= n:
            return None
        item = self.items[idx]
        if idx == n - 1:
            self.items.pop()
        else:
            self.items[idx] = self.items.pop()
            self._sift_down(idx)
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
                and self.gte(self.items[idx], r_child):
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
