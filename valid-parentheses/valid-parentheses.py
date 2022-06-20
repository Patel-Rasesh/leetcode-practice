class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. Upon encountering (, [, {, push ), ] and } to the stack respectively
        stack = []
        for sign in s:
            if sign == '[':
                stack.append('[')
            elif sign == '(':
                stack.append('(')
            elif sign == '{':
                stack.append('{')
            # 2. Upon encountering ), ], or }, pop them from the stack
            elif sign == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop(-1)
            elif sign == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop(-1)
            elif sign == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop(-1)
                
        # 3. Upon reaching the end of the string, if stack is empty, return True
        if len(stack) == 0:
            return True
        # 4. Else return False
        else:
            return False