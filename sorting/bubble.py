def bubble_sort(data):
    n = 0
    items = {}
    for item in data:
       items[n] = item
       n += 1
    for i in range(n - 2, -1, -1):
        next_item_index = n - i - 2
        for j in range(n - 1, next_item_index, -1):
            if items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
        yield items[next_item_index]
    yield items[n - 1]
