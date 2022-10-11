from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key):
        if key not in self.values:
            return -1
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]

    def put(self, key, value):
        if key not in self.values:
            if len(self.values) == self.capacity:
                self.values.popitem(last=False)
        else:
            self.values.pop(key)
        self.values[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)