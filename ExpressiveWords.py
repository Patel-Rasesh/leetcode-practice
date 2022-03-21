from collections import defaultdict
from itertools import groupby
class Solution(object):
    def expressiveWords(self, s, words):
        # Make a dictionary for s
        wordStringDict = defaultdict(int)
        for charac in s:
            wordStringDict[charac] += 1
        output = 0
        stringSet = set(s)
        #for _, group in groupby(s):
            #print(_, group)
        return ["".join(group) for _, group in groupby(s)]
        # for word in words:
        #     flag = True
        #     wordSet = set(word)
        #     # Condition checking only characters from s appear in word
        #     # If any other character appear or any character from s doesn't appear
        #     # Return False
        #     if wordSet != stringSet:
        #         break
        
            
        return output
obj = Solution()
s = "heeellooo"
words = ["hello", "hi", "helo"]
# s = "zzzzzyyyyy"
# words = ["zzyy","zy","zyy"]
print(obj.expressiveWords(s, words))

'''
wordDict = defaultdict(int)
            for charac in word:
                wordDict[charac] += 1
            for charac in wordSet:
                if  wordStringDict[charac] - wordDict[charac] == 1 or wordDict[charac] > wordStringDict[charac]:
                    flag = False
                    break
            if flag == True:
                output += 1
'''