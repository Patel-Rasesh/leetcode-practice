def solution(A, B):
    return removeZeroFromEnd(positiveSum([0], findSum(A) + findSum(B), 0))
def findSum(A):
    total = 0
    for i in range(len(A)):
        total += A[i]*pow(-2, i)
    return total
def positiveSum(result, sum, index):
    if(findSum(result) == sum):
        return result
    if(sum < 0):
        if(findSum(result) < sum):
            return flipToZero(result, sum, index-2, index-2)
    else:
        if(findSum(result) > sum):
            return flipToZero(result, sum, index-2, index-2)
    result.append(0)
    result[index] = 1
    result.append(0)
    index += 2
    return positiveSum(result, sum, index)
def flipToZero(result, sum, index, bringBackIndex):
    if(findSum(result) == sum):
        return result
    if(sum < 0):
        if(findSum(result) > sum):
            return positiveSum(result, sum, 1)  
    else:
        if(findSum(result) < sum):
            return positiveSum(result, sum, 0)  
    if(index == 0 or index == 1):
        return negativeSum(result, sum, bringBackIndex-1, bringBackIndex-1)
    index -= 2
    result[index] = 0
    return flipToZero(result, sum, index, bringBackIndex)

def negativeSum(result, sum, index, bringBackIndex):
    if(findSum(result) == sum):
        return result
    if(sum < 0):
        if(findSum(result) > sum):
            return positiveSum(result, sum, 1)
    else:
        if(findSum(result) < sum):
            return positiveSum(result, sum, 0)
    if(index == 0 or index == 1):
        return negativeSum(result, sum, index, bringBackIndex-1)
    result[index] = 1
    index -= 2
    return negativeSum(result, sum, index)

def removeZeroFromEnd(output):
    if(output[-1] != 0):
        return output
    output.pop()
    return removeZeroFromEnd(output)
A = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
B = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1]

#print(removeZeroFromEnd(positiveSum([0], 4, 0)))
print(removeZeroFromEnd(positiveSum([0], -23, 1)))
#print(removeZeroFromEnd(positiveSum([0], -12, 1)))

#print(solution(A, B))