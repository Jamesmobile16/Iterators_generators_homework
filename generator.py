import types


def flat_generator(list_of_lists):
    counter = 0
    while counter < len(list_of_lists):
        result = []
        for item in list_of_lists:
            if type(item) != list:
                result.append(item)
                continue
            for nested_item in item:
                result.append(nested_item)
                counter += 1
        for x in result:
            yield x


# for item in flat_generator([['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]):
#     print(item)

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()