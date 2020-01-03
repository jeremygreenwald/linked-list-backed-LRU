from linked_list import DoubleLinkedList


class LRUCache:
    class Node:
        def __init__(self, value, access_ref):
            self.value = value
            self.access_ref = access_ref

    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = {}
        self.accesses = DoubleLinkedList()

    def set(self, key, value):
        self._evict()
        if key in self.cache:
            list_ref = self.cache[key].access_ref
            self.accesses.remove(list_ref)
            self.accesses._append(list_ref)
        else:
            list_ref = self.accesses.append(key)

        self.cache[key] = LRUCache.Node(value, list_ref)

    def get(self, key):
        if key not in self.cache:
            raise ValueError('{} not found in cache'.format(key))

        list_ref = self.cache[key].access_ref
        self.accesses.remove(list_ref)
        self.accesses._append(list_ref)
        return self.cache[key].value

    def _evict(self):
        if self.max_size == len(self.cache):
            node = self.accesses.front
            self.accesses.remove(node)
            del self.cache[node.value]
