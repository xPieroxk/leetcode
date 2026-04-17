class Node:
    def __init__(self, prev=None, next=None, key=0, val=0):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del self.map[node.key]

    def insert(self, node):
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.map[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        n = self.map[key]
        self.remove(n)
        self.insert(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        self.insert(Node(key=key, val=value))
        if len(self.map) > self.capacity:
            self.remove(self.head.next)
