nums = [5, 2, 6, 1]
print(nums)
tempStorage = [0] * len(nums)
count = 0
resultCount = []

for index1 in range(len(nums)):
    for index2 in range(index1+1, len(nums)):
        if((nums[index2] - nums[index1]) < 0):
            count += 1
    resultCount.append(count)
    count = 0
print(resultCount)