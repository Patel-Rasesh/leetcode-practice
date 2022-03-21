from sympy import NumberSymbol
nums = [1,2,3,4,5,6,7]
k = 3

#nums = [-1, -100, 3, 99]
#k = 2

def rotateOnce(nums, k):
    if k == 0:
        return nums
    tempNumber = nums[-1]
    for index in range(len(nums)):
        nums[index], tempNumber = tempNumber, nums[index]
    k -= 1
    return rotateOnce(nums, k)
    
rotateOnce(nums, k)
print(nums)