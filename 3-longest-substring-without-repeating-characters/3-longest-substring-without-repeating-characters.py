class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # inputCharac = list(s)
        # score = defaultdict(int)
        # result = []
        # count, runner = 0, 0
        # while(runner < len(inputCharac)):
        #     for i, character in enumerate(inputCharac[runner:]):
        #         if(score[character] == 1):
        #             result.append(count)
        #             count = 0
        #             runner += 1
        #             # Reset the dictionary too
        #             score.clear()
        #             break
        #         score[character] += 1
        #         count += 1
        # if result:
        #     return max(result)
        # else:
        #     return 0
        
        
        # AMAZON INTERVIEW PREP
        
        # TODO - change this to set
        substringSet = []
        
        masterIndex = 0
        while masterIndex < len(s) and masterIndex != len(s)-1:
            # Iterate through the string
            # TODO - Use extend in list/set and remove tempString
            uniqueSubstring = set()

            tempString = ""
            for slaveIndex in range(masterIndex, len(s)):

                # Check if the set has that character, if not add it
                # If yes, save that substring to result set
                if s[slaveIndex] in uniqueSubstring:
                    substringSet.append(tempString)
                    
                    break
                elif slaveIndex == len(s)-1:
                    tempString += s[slaveIndex]
                    substringSet.append(tempString)
                    
                    break
                uniqueSubstring.add(s[slaveIndex])
                tempString += s[slaveIndex]
            masterIndex += 1
            
        # Sort the result set by length of the elements and return the largest
        
        substringSet = sorted(substringSet, key=lambda x:len(x), reverse=True)
        print(substringSet)
        
        if len(substringSet):
            return len(substringSet[0]) 
        elif len(s) == 1:
            return len(s)
        else:
            return 0
        