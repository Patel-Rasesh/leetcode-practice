# Time and memory were exceeding with the following code
# def checkSequence(number):
#     if(number // 10 == 0):
#         return True
#     if(number % 10 != (number//10)%10 + 1):
#         return False
#     return checkSequence(number//10)

# #print(checkSequence(45678))

# def sequentialDigits(low, high):
#     resultantArray = []
#     for eachNumber in range(low, high+1):
#         if(checkSequence(eachNumber) == True):
#             resultantArray.append(eachNumber)
#     return resultantArray

# outputArray = sequentialDigits(1000, 13000)

# print(outputArray)

# Approach two - Sliding window

from ast import Pass

from sympy import resultant


sampleSet = "123456789"
low = 100
high = 300
result = []
for length in range(len(str(low)), len(str(high))+1):
    for startingPoint in range(len(sampleSet)+1 - length):
        tempNumber = int(sampleSet[startingPoint:length+startingPoint])
        if(tempNumber >= low and tempNumber <= high):
            result.append(tempNumber)
print(result)