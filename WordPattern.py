pattern = 'aaaa'
s = "dog cat cat dog"
wordList = s.split(' ')
wordDict = {}
for i, alpha in enumerate(pattern):
    if alpha in wordDict:
        if wordDict[alpha] == wordList[i]:
            continue
        else:
            print("False")
    else:
        wordDict[alpha] = wordList[i]
if(len(set(wordList)) == len(set(pattern))):
    print("True")
else:
    print("False")