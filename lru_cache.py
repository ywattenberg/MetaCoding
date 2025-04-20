from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise AttributeError('Expected positive capacity')

        self.cache: dict[int, int] = {}
        self.capacity = capacity
        self.access: deque[int] = deque()
        self.num_access: dict[int, int] = {}
        # keep track of num accesses to each element and deque for history advance until 1 found

    def _find_next(self):
        for _ in range(len(self.access)):
            curr = self.access[-1]
            if curr not in self.cache or self.num_access[curr] > 1:
                self.access.pop()
                if curr in self.num_access:
                    self.num_access[curr] -= 1
            else:
                break

    def get(self, key: int) -> int:
        if key in self.cache:
            self.num_access[key] += 1
            self.access.appendleft(key)
            self._find_next()
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.access.appendleft(key)
        if key not in self.num_access:
            if len(self.cache) > self.capacity:
                self._find_next()
                lru_key = self.access.pop()
                del self.cache[lru_key]
                del self.num_access[lru_key]
            self.num_access[key] = 0
        self.num_access[key] += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
