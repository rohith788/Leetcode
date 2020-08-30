class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.last = []

    def get(self, key: int) -> int:
        if key in self.map.keys():
            if key in self.last:
                self.last.remove(key)
                self.last.append(key)
            return self.map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.last.remove(key)
        elif len(self.map) >= self.capacity:
            self.map.pop(self.last.pop(0))
        self.last.append(key)
        self.map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)