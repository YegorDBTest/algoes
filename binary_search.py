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


def binary_search_nearest(data, item):
    '''
    Binary search witch returns data of max lower index and min higher index.

    data - sorted list.
    item - item to search in data.

    Average complexity - O(log n).
    '''

    lower_index = 0
    higher_index = len(data) - 1
    max_lower_index = None
    min_higher_index = None
    while higher_index >= lower_index:
        half_index = lower_index + (higher_index - lower_index) // 2
        if item == data[half_index]:
            return half_index, None, None
        elif item > data[half_index]:
            max_lower_index = half_index
            lower_index = half_index + 1
        else:
            min_higher_index = half_index
            higher_index = half_index - 1
    return -1, max_lower_index, min_higher_index
