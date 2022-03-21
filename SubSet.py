nums = [1,2,3]
output = [[]]
for num in nums:
    output += [curr + [num] for curr in output]
print(output)