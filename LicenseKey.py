class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.upper().replace('-', '')[::-1]
        output = ""
        groupLength = 0
        for charac in s:
            if groupLength == k:
                output += '-'
                groupLength = 0
            output += charac
            groupLength += 1
        return output[::-1]
obj = Solution()
s = "2-5g-3-J"
k = 2
print(obj.licenseKeyFormatting(s, k))