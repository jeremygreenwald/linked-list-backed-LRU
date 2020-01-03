

class DoubleLinkedList:
    class Node:
        def __init__(self, value, prev=None, next_=None):
            self.value = value
            self.prev = prev
            self.next = next_

    class Iter:
        def __init__(self, node):
            self.ref = node

        def __next__(self):
            if self.ref is None:
                raise StopIteration
            else:
                value = self.ref.value
                self.ref = self.ref.next
                return value

    def __init__(self):
        self.front = None
        self.end = None

    def __iter__(self):
        return DoubleLinkedList.Iter(self.front)

    def append(self, value):
        node = DoubleLinkedList.Node(value)
        return self._append(node)

    def _append(self, node):
        if self.end:
            self.end.next = node
            node.prev = self.end

        if not self.front:
            self.front = node

        self.end = node
        return node

    def prepend(self, value):
        node = DoubleLinkedList.Node(value)
        return self._prepend(node)

    def _prepend(self, node):
        if self.front:
            self.front.prev = node
            node.next = self.front

        if not self.end:
            self.end = node

        self.front = node
        return node

    def insert_after(self, location, value):
        node = DoubleLinkedList.Node(value)
        self._insert_after(location, node)

    def _insert_after(self, location, node):
        n = location.next
        location.next = node
        node.prev = location
        node.next = n

        if self.end == location:
            self.end = node
        else:
            n.prev = node

    def remove(self, node):
        n = node.next
        p = node.prev
        if self.front == node and self.end == node:
            self.front = None
            self.end = None
        elif self.front == node:
            self.front = n
            self.front.prev = None
        elif self.end == node:
            self.end = p
            self.end.next = None
        else:
            n.prev = p
            p.next = n
