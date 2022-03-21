class ShiftToRight:
    arr = []
    def shiftRight(self, i):
        for a in range(len(self.arr)-1,i,-1):
            self.arr[a] = self.arr[a-1]

    def duplicateZeros(self, a):
        self.arr = a
        i = 0
        while i < len(self.arr):
            if self.arr[i] == 0:
                self.shiftRight(i)
                i += 1
            i += 1
            
        return self.arr

a = [1,2,3]
obj = ShiftToRight()
print(obj.duplicateZeros(a))