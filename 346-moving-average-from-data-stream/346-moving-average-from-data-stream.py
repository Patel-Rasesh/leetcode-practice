class MovingAverage:

    def __init__(self, size: int):
        
        self.array = []
        self.capacity = size
    def next(self, val: int) -> float:
        self.array.append(val)
        total = sum(self.array[-self.capacity:])
        temp1 = total
        temp2 = min(len(self.array), self.capacity)
        return temp1/temp2


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)