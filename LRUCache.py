class LRUCache:
    q = []
    capacity = 0
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = []
    def get(self, key):
                
        for i, element in enumerate(self.q):
            if key == element[0]:
                temp = self.q.pop(i)[1]
                self.q.append([key, temp])
                return temp
        else:
            return -1
    def put(self, key, value):
        
        for i, element in enumerate(self.q):
            if key == element[0]:
                self.q.pop(i)
                self.q.append([key, value])
                return
        
        self.q.append([key, value])
        if len(self.q) > self.capacity:
            self.q.pop(0)
        return

object = LRUCache(2)
object.put(1,1)
object.put(2,2)
print(object.get(1))
object.put(3,3)
print(object.get(2))
object.put(4,4)
print(object.get(1))
print(object.get(3))
print(object.get(4))