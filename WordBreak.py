# inputStr = "applepenapples"
# wordList = ["apple", "pen"]
# # List to verify output
# mergeCharac = []
# # Stores words from the inputString, if they occur in word dictionary
# tempWord = inputStr[0]

# flag = True
# runner = 0
# for i, charac in enumerate(inputStr[runner:]):
#     flag = True
#     for word in wordList:
#         if(tempWord == word):
#             mergeCharac.append(tempWord)
#             if(i != (len(inputStr) - 1)):
#                 tempWord = inputStr[i+1]
#                 runner = i+1
#             flag = False
#             break
#     if(flag == True and (i != (len(inputStr) - 1))):
#         tempWord += inputStr[i+1]

# print(mergeCharac)

import numpy as np
a = np.array([[1,2,3], [4,5,8]])

print(a)