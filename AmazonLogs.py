#logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key","a8 act zoo"]
for log in logs:
    paper = log.split(" ", maxsplit = 1)
    print(paper)
# digitIndex = []
# wordDict = {}
# for i, log in enumerate(logs):
#     logArray = log.split(" ")
#     if logArray[1].isdigit() == True:
#         digitIndex.append(i)
#     else:
#         wordDict[logArray[0]] = logArray[1:]
# print(wordDict)
# print(digitIndex)
# print(sorted(wordDict.items(), key=lambda kv: kv[1]))

# # You are using extra space to place your input back in - avoid that

# result = ""
# resultArray = []
# for key in wordDict:
#     result = key
#     for eachValue in wordDict[key]:
#         result += ' '
#         result += eachValue

#     resultArray.append(result)
# for index in digitIndex:
#     resultArray.append(logs[index])

# print("Printing original")
# print(logs)
# print("Printing output")
# print("----------------")
# print(resultArray)