def binary_search(data, item):
    '''
    Binary search.

    data - sorted list.
    item - item to search in data.

    Average complexity - O(log n).
    '''

    lower_index = 0
    higher_index = len(data) - 1
    while higher_index >= lower_index:
        half_index = lower_index + (higher_index - lower_index) // 2
        if item == data[half_index]:
            return half_index
        elif item > data[half_index]:
            lower_index = half_index + 1
        else:
            higher_index = half_index - 1
    return -1
