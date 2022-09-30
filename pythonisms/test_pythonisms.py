import pytest
from pythonisms import LinkedList, emphasize

def test_string():
    chars = LinkedList(('a', 'b', 'c'))
    actual = str(chars)
    expected = '{ a } -> { b } -> { c } -> None'
    assert actual == expected


def test_for_in():
    chars = LinkedList(('a', 'b', 'c'))
    actual = []

    for char in chars:
        actual.append(char)

    expected = ['a', 'b', 'c']
    assert actual == expected


def test_list_comprehension():
    chars = LinkedList(('a', 'b', 'c'))
    actual = [char.upper() for char in chars]
    expected = ['A', 'B', 'C']
    assert actual == expected


def test_list_cast():
    expected = ['a', 'b', 'c']
    actual = LinkedList(expected)
    assert list(actual) == expected


def test_length():
    actual = LinkedList(range(1, 21))
    expected = 20
    assert len(actual) == expected


def test_filter():
    nums = LinkedList(range(1, 21))
    actual = [num for num in nums if num % 2]
    expected = [1,3,5,7,9,11,13,15,17,19]
    assert actual == expected


def test_next():
    chars = LinkedList(('a', 'b', 'c'))
    iterator = iter(chars)
    assert next(iterator) == 'a'
    assert next(iterator) == 'b'
    assert next(iterator) == 'c'


def test_stop_iteration():
    chars = LinkedList(('a', 'b', 'c'))
    iterator = iter(chars)

    with pytest.raises(StopIteration):
        while True:
            char = next(iterator)


def test_equals():
    list_a = LinkedList(('a', 'b', 'c'))
    list_b = LinkedList(('a', 'b', 'c'))
    assert list_a == list_b


def test_inequal():
    list_a = LinkedList(('a', 'b', 'c'))
    list_b = LinkedList(('a', 'c', 'b'))
    assert list_a != list_b


def test_get_item():
    chars = LinkedList(('a', 'b', 'c'))
    actual = chars[1]
    expected = 'b'
    assert actual == expected


def test_get_item_out_of_range():
    chars = LinkedList(('a', 'b', 'c'))
    with pytest.raises(IndexError):
        actual = chars[20]


def test_emphasize():
    @emphasize
    def talk():
        return 'hey'

    actual = talk()
    expected = 'hey!!!'
    assert actual == expected