def shiftByOne(a, startingPoint):
    for i in reversed(range(startingPoint, len(a))):
        a[i] = a[i-1]
    a[startingPoint] = 0

a = [1, 0, 2, 3, 4]

for i in range(len(a)):
    if(a[i] == 0):
        shiftByOne(a, i)
        break
        #i = i + 2
print(a)