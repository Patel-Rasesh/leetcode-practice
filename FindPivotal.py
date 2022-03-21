nums = [-1,-1,-1,-1,-1,-1]

total = sum(nums)
totalLeft = 0

if total is nums[0]:
    print(0)
elif total is nums[-1]:
    print(len(nums)-1)
for element in range(len(nums)):
    if totalLeft == (total - totalLeft - element):
        print(element)
    totalLeft += nums[element]
print(-1)