import sys
prices = [2, 4, 1, 5]
#prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
profit = 0
minPrice = sys.maxsize

for price in prices:
    if(minPrice > price):
        minPrice = price
    elif(price - minPrice > profit):
        profit = price - minPrice
print(profit)


