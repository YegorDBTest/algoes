def insertion_sort(items):
    '''
    Pure insertion sort.

    items - list of comparable items.

    ```python
    >>> items = [1, 9, 5, 2, 7, 3, 8, 4, 6]
    >>> insertion_sort(items)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

    Total time cost:
    ~ O(n^2)
    '''

    n = len(items) # O(1)
    for i in range(1, n): # O(n - 1)
        for j in range(i, 0, -1): # from O(1) to O(n / 2)
            if items[j] < items[j - 1]:
                items[j - 1], items[j] = items[j], items[j - 1]
            else:
                break
    return items
