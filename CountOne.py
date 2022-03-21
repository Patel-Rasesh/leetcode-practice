nums = [1,0,1,1,0,1]

def countOne(nums):
    output = []
    index = 0
    exit = False
    while(exit != True):
        flag = True
        ones = 0
        for i in range(index, len(nums)):
            if i == len(nums) - 1:
                if nums[i] == 1:
                    ones += 1
                output.append(ones)
                exit = True
                break
            elif nums[i] == 1:
                ones += 1
                continue
            elif nums[i] == 0 and flag == True:
                ones += 1
                flag = False
                index = i+1
                continue
            elif nums[i] == 0 and flag == False:
                output.append(ones)
                break
    return max(output)
print(countOne(nums))