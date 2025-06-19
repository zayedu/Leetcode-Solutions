

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)          # mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # Insert or update
        self.cache[key] = value
        self.cache.move_to_end(key)          # most recently used

        # Evict if over capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)   # remove least-recently-used



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
