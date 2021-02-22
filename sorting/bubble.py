def bubble_sort(items):
    '''
    Pure bubble sort.

    items - list of comparable items.

    ```python
    >>> items = [1, 9, 5, 2, 7, 3, 8, 4, 6]
    >>> sorted_items = bubble_sort(items)
    >>> sorted_items
    <generator object bubble_sort at 0x7fc467d3d820>
    >>> tuple(sorted_items)
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ```

    Total time cost:
    ~ O(n^2)
    '''

    n = len(items) # O(1)
    for i in range(n - 2, -1, -1): # O(n - 1)
        next_item_index = n - i - 2
        for j in range(n - 1, next_item_index, -1): # O(n / 2)
            if items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
        yield items[next_item_index]
    yield items[n - 1]


def bubble_sort_with_need_to_swap_check(items):
    '''
    Bubble sort with need to swap check.

    items - list of comparable items.

    ```python
    >>> items = [1, 9, 5, 2, 7, 3, 8, 4, 6]
    >>> sorted_items = bubble_sort_with_need_to_swap_check(items)
    >>> sorted_items
    <generator object bubble_sort_with_need_to_swap_check at 0x7fc467d3d190>
    >>> tuple(sorted_items)
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ```

    Total time cost:
    ~ O(n^2)
    '''

    n = len(items) # O(1)
    need_to_swap = True
    for i in range(n - 2, -1, -1): # O((n - 1) / 2)
        next_item_index = n - i - 2
        if need_to_swap:
            need_to_swap = False
            for j in range(n - 1, next_item_index, -1):
                '''
                from O(n - 1) (if outer cycle contains 1 iteration)
                to O(n / 2) (if outer cycle contains n - 1 iteration)
                '''
                if items[j] < items[j - 1]:
                    items[j], items[j - 1] = items[j - 1], items[j]
                    need_to_swap = True
        yield items[next_item_index]
    yield items[n - 1]
