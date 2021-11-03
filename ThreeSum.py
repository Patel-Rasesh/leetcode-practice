def findTriplets(arr):
    duplicate, result= set(), set()
    ref = {}
    for i, num1 in enumerate(arr):
        if num1 is not duplicate:
            duplicate.add(num1)
            for j, num2 in enumerate(arr[i+1:]):
                thirdDigit = -num1 - num2
                if thirdDigit in ref and ref[thirdDigit] == i:
                    result.add(tuple(sorted((num1, num2, thirdDigit))))
                ref[num2] = i
    return result

array = [-1,0,1,2,-1,4]
answer = findTriplets(array)

print(answer)
