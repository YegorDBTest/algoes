def merge(items1, items2):
    '''
    Merge.

    items1 - sorted list.
    items2 - sorted list.

    ```python
    >>> items1 = [1, 3, 6]
    >>> items2 = [2, 4, 5]
    >>> merged_items = merge(items1, items2)
    >>> merged_items
    [1, 2, 3, 4, 5, 6]
    ```

    Total time cost:
    ~ O(n1 + n2)
    '''

    result = []
    n1 = len(items1)
    i1 = 0
    n2 = len(items2)
    i2 = 0
    for i in range(n1 + n2):
        if items1[i1] < items2[i2]:
            result.append(items1[i1])
            i1 += 1
            if i1 == n1:
                result += items2[i2:]
                break
        else:
            result.append(items2[i2])
            i2 += 1
            if i2 == n2:
                result += items1[i1:]
                break
    return result


def merge_sort(items):
    '''
    Merge sort.

    items - list of comparable items.

    ```python
    >>> items = [1, 9, 5, 2, 7, 3, 8, 4, 6]
    >>> sorted_items = merge_sort(items)
    >>> sorted_items
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

    Total time cost:
    ~ O(n * log(n))
    '''

    n = len(items)
    if n == 1:
        return items
    middle = n // 2;
    return merge(merge_sort(items[0:middle]), merge_sort(items[middle:]))
