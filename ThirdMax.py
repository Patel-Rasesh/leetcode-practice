import heapq
nums = [2, 2, 3, 1]
thirdMax = heapq.nlargest(3, set(nums))[-1]
print(thirdMax)
    # if(thirdMax):
    #     print(thirdMax)
    # else:
    #     print(max(nums))