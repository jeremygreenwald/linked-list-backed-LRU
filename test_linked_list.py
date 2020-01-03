import pytest

from linked_list import DoubleLinkedList


def assert_contains(actual, expected):
    actual_it = iter(actual)
    expected_it = iter(expected)
    for _ in range(len(expected)):
        assert next(actual_it) == next(expected_it)

    # linked list iterator should be at end
    with pytest.raises(StopIteration):
        next(actual_it)


def test_linked():
    l = DoubleLinkedList()
    l.append(5)
    assert l.front.value == 5
    assert l.end.value == 5


def test_linked_2():
    l = DoubleLinkedList()
    l.append(5)
    l.append(7)
    assert l.front.value == 5
    assert l.front.next.value == 7
    assert l.end.value == 7
    assert_contains(l, [5, 7])


def test_linked_prepend():
    l = DoubleLinkedList()
    l.prepend(5)
    assert l.front.value == 5
    assert l.end.value == 5
    assert_contains(l, [5])


def test_linked_prepend_2():
    l = DoubleLinkedList()
    l.prepend(5)
    l.prepend(7)
    assert l.front.value == 7
    assert l.front.next.value == 5
    assert l.end.value == 5
    assert_contains(l, [7, 5])


def test_insert_after():
    l = DoubleLinkedList()
    l.append(5)
    l.append(7)
    l.append(9)
    l.insert_after(l.front, 13)
    assert l.front.next.value == 13
    assert_contains(l, [5, 13, 7, 9])


def test_insert_after_2():
    l = DoubleLinkedList()
    l.append(5)
    l.insert_after(l.front, 13)
    assert l.end.value == 13
    assert_contains(l, [5, 13])


def test_remove():
    l = DoubleLinkedList()
    l.append(5)
    l.append(7)
    l.append(9)
    l.remove(l.front.next)
    assert l.front.value == 5
    assert l.front.next.value == 9
    assert_contains(l, [5, 9])


def test_remove_2():
    l = DoubleLinkedList()
    l.append(5)
    l.append(7)
    l.append(9)
    l.remove(l.end)
    assert l.front.value == 5
    assert l.end.value == 7
    assert_contains(l, [5, 7])


def test_remove_3():
    l = DoubleLinkedList()
    l.append(5)
    l.append(7)
    l.append(9)
    l.remove(l.front)
    assert l.front.value == 7
    assert l.end.value == 9
    assert_contains(l, [7, 9])


def test_remove_4():
    l = DoubleLinkedList()
    l.append(5)
    l.remove(l.front)
    assert l.front is None
    assert l.end is None
    assert_contains(l, [])


def test_remove_5():
    l = DoubleLinkedList()
    l.append(5)
    l.append(7)
    l.remove(l.front)
    assert l.front.value == 7
    assert l.end is not None
    assert_contains(l, [7])


def test_remove_6():
    l = DoubleLinkedList()
    l.append(5)
    l.append(7)
    l.remove(l.end)
    assert l.front.value == 5
    assert l.end is not None
    assert_contains(l, [5])
