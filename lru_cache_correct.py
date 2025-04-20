from typing import Optional


class Node:
    def __init__(
        self, value: int, prev: Optional['Node'], next: Optional['Node'], key: int = -1
    ):
        self.value = value
        self.prev = prev
        self.next = next
        self.key = key

    def remove(self):
        assert self.prev and self.next, 'tried to del dummy node'
        self.prev.next = self.next
        self.next.prev = self.prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.start = Node(-1, None, None)
        self.end = Node(-1, self.start, None)
        self.start.next = self.end
        self.nodes: dict[int, Node] = {}

    def increase_prio(self, key: int) -> None:
        node = self.nodes[key]
        node.remove()
        node.prev = self.start
        node.next = self.start.next
        node.next.prev = node
        self.start.next = node

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.increase_prio(key)
            return self.nodes[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.increase_prio(key)
            self.nodes[key].value = value
        else:
            if len(self.nodes) >= self.capacity:
                del self.nodes[self.end.prev.key]
                self.end.prev.remove()
            node = Node(value, self.start, self.start.next, key=key)
            self.nodes[key] = node
            self.start.next = node
            node.next.prev = node  # type:ignore


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
