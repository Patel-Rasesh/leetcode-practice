class Solution(object):
    def reverseWords(self, s):
        splitString = self.customSplit(s)
        result = ' '.join(splitString[::-1])
        return result
    def customSplit(self, s):
        output = []
        tempString = ''
        for charac in s:
            if (charac == ' '):
                if tempString == '':
                    continue
                output.append(tempString)
                tempString = ''
            else:
                tempString += charac
        if tempString != '':
            output.append(tempString)
        return output
            
obj = Solution()
s = "a good   example"
print(obj.reverseWords(s))