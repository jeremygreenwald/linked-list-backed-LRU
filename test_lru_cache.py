import pytest

from lru_cache import LRUCache


def test_lru_cache():
    c = LRUCache(10)
    c.set('a', 3)
    assert c.get('a') == 3


def test_lru_cache_2():
    c = LRUCache(10)
    c.set('a', 3)
    c.set('b', 13)
    c.set('c', 23)
    c.set('a', 33)
    assert c.get('a') == 33
    assert c.get('b') == 13
    assert c.get('c') == 23


def test_lru_cache_max_size():
    c = LRUCache(1)
    c.set('a', 3)
    c.set('b', 33)
    assert c.get('b') == 33
    with pytest.raises(ValueError):
        c.get('a')


def test_lru_cache_max_size_2():
    c = LRUCache(2)
    c.set('a', 3)
    c.set('b', 5)
    c.set('c', 7)
    c.set('d', 9)
    c.set('e', 11)
    c.set('f', 13)
    assert c.get('e') == 11
    assert c.get('f') == 13
    with pytest.raises(ValueError):
        c.get('d')


def test_lru_cache_max_size_with_get():
    c = LRUCache(3)
    c.set('a', 3)
    c.set('b', 5)
    c.set('c', 7)
    assert c.get('a') == 3
    c.set('d', 9)
    assert c.get('a') == 3
    assert c.get('c') == 7
    assert c.get('d') == 9
    with pytest.raises(ValueError):
        c.get('b')
