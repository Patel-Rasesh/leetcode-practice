class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        masterString = ''
        for charac in s:
            if charac != ']':
                stack.append(charac)
                continue
            subString = ''
            while stack[-1] != '[':
                subString += stack.pop(-1)
            
            # Popping the open bracket
            stack.pop(-1)
            
            # string = ''
            # stack.pop(-1) until the next open bracket, close bracket or
            # an alphabet
            iterString = ''
            while stack and stack[-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                iterString += stack.pop(-1)
            
            print(iterString)
            iteration = int(iterString[::-1])
            for _ in range((iteration)):
                for eachCharac in range(len(subString)-1, -1, -1):
                    stack.append(subString[eachCharac])
                    # stack.append(subString[::-1])
            
        for string in stack:
            masterString += string
        
        return masterString
        
            