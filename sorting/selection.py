def selection_sort(items):
    '''
    Pure selection sort.

    items - list of comparable items.

    ```python
    >>> items = [1, 9, 5, 2, 7, 3, 8, 4, 6]
    >>> sorted_items = selection_sort(items)
    >>> sorted_items
    <generator object selection_sort at 0x7f20ef58d820>
    >>> tuple(sorted_items)
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ```

    Total time cost:
    ~ O(n^2)
    '''

    n = len(items) # O(1)
    for i in range(n - 1): # O(n - 1)
        for j in range(i + 1, n): # O(n / 2)
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
        yield items[i]
    yield items[n - 1]


def double_selection_sort(items):
    '''
    Double selection sort.

    items - list of comparable items.

    ```python
    >>> items = [1, 9, 5, 2, 7, 3, 8, 4, 6]
    >>> sorted_items = double_selection_sort(items)
    >>> sorted_items
    <generator object double_selection_sort at 0x7f45aaaa1580>
    >>> tuple(sorted_items)
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ```

    Total time cost:
    ~ O(n^2)
    '''

    n = len(items) # O(1)
    for i in range(n - 1): # O(n - 1)
        latest = n - i - 1
        for j in range(i, latest): # O(n / 4)
            if items[latest] < items[j]:
                items[latest], items[j] = items[j], items[latest]
            if items[i] > items[j + 1]:
                items[i], items[j + 1] = items[j + 1], items[i]
        yield items[i]
    yield items[n - 1]
