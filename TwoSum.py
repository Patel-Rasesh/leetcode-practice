#array elements and target sum could be negative integers
class TwoSum:


    def extractIndices(inputArray, target):
        
    #     for i in range(len(inputArray)):
    #         firstNumber = inputArray[i]
    #         secondNumber = target - firstNumber
    #         for j in range(i+1, len(inputArray)):
    #             if(inputArray[j] == secondNumber):
    #                 return i, j
            
    #     return -1, -1
        h= {}
        for i, num in enumerate(inputArray):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

    inputArray = [-12, -45, -68, 20, 74, -11, 150]
    target = 224
    a, b = extractIndices(inputArray, target)
    print("Indices are - ", a, " and ", b)