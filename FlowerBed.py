flowerbed = [0,0,1,0,1]
n = 1
count = 1
if(n == 0):
    print("True")

for i, pot in enumerate(flowerbed):
    if(pot == 0):
        count += 1
    else:
        count = 0
    if count == 3:
        n -= 1
        count = 1
    if count == 2 and i == len(flowerbed) -1 and flowerbed[i] == 0:
        n -= 1
    if(n == 0):
        print("True")
        break