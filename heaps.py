import math


class BaseHeap:

    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        self._up_item(len(self._items))

    def extract_item(self, index):
        if index > len(self._items):
            return None
        item = self._items[index - 1]
        if index == len(self._items):
            self._items.pop()
        else:
            self._items[index - 1] = self._items.pop()
            self._down_item(index)
        return item

    def _up_item(self, index):
        while index > 1:
            parent_index = math.floor(index / 2)
            i = index - 1
            pi = parent_index - 1
            if self._check_parent_and_child(pi, i):
                break
            self._items[pi], self._items[i] = self._items[i], self._items[pi]
            index = parent_index

    def _down_item(self, index):
        while True:
            child_index = None
            for i in range(2):
                chi = index * 2 + i
                if chi > len(self._items):
                    continue
                pci = child_index - 1 if child_index else None
                if self._check_parent_and_childs(index - 1, chi - 1, pci)
                    child_index = chi
            if not child_index:
                break
            i = index - 1
            ci = child_index - 1
            self._items[ci], self._items[i] = self._items[i], self._items[ci]
            index = child_index


class MinHeap(BaseHeap):

    def _check_parent_and_child(self, parent_index, child_index):
        return self._items[parent_index] <= self._items[child_index]

    def _check_parent_and_childs(self, parent_index, child_index, prev_child_index):
        return (
            self._items[child_index] < self._items[parent_index]
            and (prev_child_index is None
                 or self._items[child_index] < self._items[prev_child_index])
        )


class MaxHeap(BaseHeap):

    def _check_parent_and_child(self, parent_index, child_index):
        return self._items[parent_index] >= self._items[child_index]

    def _check_parent_and_childs(self, parent_index, child_index, prev_child_index):
        return (
            self._items[child_index] > self._items[parent_index]
            and (prev_child_index is None
                 or self._items[child_index] > self._items[prev_child_index])
        )
