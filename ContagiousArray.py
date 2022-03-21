nums = [0,1,0,0,1,1,0]
countDict = {}
countDict[0] = -1
count = 0
maxLength = 0

for i, num in enumerate(nums):
    if num == 0:
        count -= 1
    else:
        count += 1
    # if count exists in dictionary, maxlength becomes its previous value and i-countDict[count]
    if count in countDict:
        maxLength = max(maxLength, i-countDict[count])
    else:
        countDict[count] = i

print(maxLength)