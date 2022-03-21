a = [1, 2, 3, 4]
# consecutive element pairing 
# for i in range(len(a)):
#     print(list(zip(a, a[1:])))

import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

for i in range(1, len(a)+1):
    print(findsubsets(a,i))
# Need to print each subset of this

# combination = [[]]
# for element in a:
#     for comb in combination:
#         combination += [comb + [element]]

# print(combination)
# output = [[]]
# exception = [[1,2], [2,3]]
# for num in a:
#     output+=[curr + [num] for curr in output]
# print(intersection(output, exception))

# print(output)
# for element in exception:
#     for subset in range(len(output)):
#         if output[subset] is element:
#             output.pop(subset)

# print(output)