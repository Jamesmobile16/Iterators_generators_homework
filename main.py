list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

class FlatIterator:

    def __init__(self, list_of_list):
        self.input = list_of_list
        self.result = []

    def __iter__(self):
        for item in self.input:
            if type(item) != list:
                self.result.append(item)
                continue
            for nested_item in item:
                self.result.append(nested_item)
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == len(self.result):
            raise StopIteration
        item = self.result[self.counter]
        self.counter += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()