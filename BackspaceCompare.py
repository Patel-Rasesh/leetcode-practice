class Solution(object):
    def backspaceCompare(self, s, t):
        print(self.getRefinedString(s))
        print(self.getRefinedString(t))
        if self.getRefinedString(s) == self.getRefinedString(t):
            return True
        else:
            return False
    def getRefinedString(self, str):
        pointer = 0
        strList = []
        for pointer, charac in enumerate(str):
            if charac == '#' and pointer == 0:
                continue
            elif charac == '#':
                if strList:
                    strList.pop(-1)
            else:
                strList.append(charac)

        return "".join(strList)

obj = Solution()
s = "ab#"
t = "c#d"
print(obj.backspaceCompare(s,t))