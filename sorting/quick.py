def quick_sort_partition(items, l, r):
    '''
    Quick sort partition.

    items - list of comparable items.
    l - start index
    r - end index

    ```python
    >>> items = [3, 5, 2, 1, 6, 4]
    >>> m = quick_sort_partition(items)
    >>> m
    2
    >>> items
    [1, 2, 3, 5, 6, 4]
    ```

    returns partition element index

    Total time cost:
    ~ O(n)
    '''

    x = items[l]
    j = l
    for i in range(l + 1, r + 1):
        if items[i] < x:
            j += 1
            items[j], items[i] = items[i], items[j]
    items[j], items[l] = items[l], items[j]
    return j


def quick_sort(items, l=0, r=None):
    '''
    Quick sort.

    items - list of comparable items.
    l - start index
    r - end index

    ```python
    >>> items = [1, 9, 5, 2, 7, 3, 8, 4, 6]
    >>> quick_sort(items)
    >>> items
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

    Total time cost:
    ~ O(n * log(n))
    '''

    if r is None:
        r = len(items) - 1
    if l >= r:
        return

    m = quick_sort_partition(items, l, r)
    quick_sort(items, l=l, r=m - 1)
    quick_sort(items, l=m + 1, r=r)


def tail_recursive_quick_sort(items, l=0, r=None):
    '''
    Tail recursive quick sort.

    items - list of comparable items.
    l - start index
    r - end index

    ```python
    >>> items = [1, 9, 5, 2, 7, 3, 8, 4, 6]
    >>> tail_recursive_quick_sort(items)
    >>> items
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

    Total time cost:
    ~ O(n * log(n))
    '''

    if r is None:
        r = len(items) - 1

    while l < r:
        m = quick_sort_partition(items, l, r)
        if m - l > r - m:
            tail_recursive_quick_sort(items, l=m + 1, r=r)
            r = m - 1
        else:
            tail_recursive_quick_sort(items, l=l, r=m - 1)
            l = m + 1
