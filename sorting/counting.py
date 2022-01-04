def counting_sort(items, m1, m2):
    '''
    Pure counting sort.

    items - list of numbers from m1 to m2.

    ```python
    >>> items = [-1, 2, 0, -2, -1, 1, 0, 2, 1, -2]
    >>> sorted_items = counting_sort(items, -2, 2)
    >>> sorted_items
    <generator object counting_sort at 0x7fb57e15e620>
    >>> tuple(sorted_items)
    (-2, -2, -1, -1, 0, 0, 1, 1, 2, 2)
    ```

    Total time cost:
    ~ O(n)
    '''

    m = m2 - m1 + 1
    counter = [0] * m

    for i in items:
        counter[i - m1] += 1

    for i in range(m):
        for j in range(counter[i]):
            yield i + m1
