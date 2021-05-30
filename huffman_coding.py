class TreeItem:
    def __init__(self, value=None, count=0):
        self.value = value
        self.count = count
        self.prefix = ''
        self.postfix = ''
        self.childrens = []

    def __lt__(self, other):
        return self.count < other.count

    def __le__(self, other):
        return self.count <= other.count

    def __gt__(self, other):
        return self.count > other.count

    def __ge__(self, other):
        return self.count >= other.count

    def __eq__(self, other):
        return self.count == other.count

    def __ne__(self, other):
        return self.count != other.count

    def __repr__(self):
        return f'({self.value}, {self.count}, {self.code})'

    def __str__(self):
        return f'({self.value}, {self.count}, {self.code})'

    @property
    def code(self):
        return f'{self.prefix}{self.postfix}'

    def add_child(self, item):
        self.childrens.append(item)
        self.count += item.count
        item.set_postfix(str(len(self.childrens) - 1))
        item.set_prefix(self.code)

    def set_prefix(self, prefix):
        self.prefix = prefix
        for item in self.childrens:
            item.set_prefix(self.code)

    def set_postfix(self, postfix):
        self.postfix = postfix


class TreeItems:
    def __init__(self, items=None):
        self.data = []
        for item in (items or []):
            self.add_item(item)

    @property
    def is_empty(self):
        return len(self.data) == 0

    def add_item(self, new_item):
        i = 0
        for item in self.data:
            if new_item >= item:
                break
            i += 1
        self.data.insert(i, new_item)

    def get_smallest_items(self):
        return [self.data.pop() for i in range(2) if self.data]


class Tree:
    def __init__(self, data_string):
        self.data = {}
        for letter in data_string:
            if letter in self.data:
                self.data[letter].count += 1
            else:
                self.data[letter] = TreeItem(value=letter, count=1)

        items = TreeItems(self.data.values())

        while not items.is_empty:
            smallest_items = items.get_smallest_items()
            if len(smallest_items) == 1:
                root = smallest_items[0]
                root.set_postfix('0')
                break
            parent = TreeItem()
            for item in smallest_items:
                parent.add_child(item)
            items.add_item(parent)


if __name__ == '__main__':
    tree = Tree('abbbbccdddddeee')
    for letter, item in tree.data.items():
        print(letter, item.code)
