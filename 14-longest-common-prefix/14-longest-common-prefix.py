class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        outputString = max(strs)
        for i in range(len(strs)):
            for j in range(i, len(strs)):
                if len(strs[i]) <= len(strs[j]):
                    subset = strs[i]
                    superset = strs[j]
                else:
                    subset = strs[j]
                    superset = strs[i]
                commonString = ""
                for a in range(len(subset)):
                    if subset[a] == superset[a]:
                        commonString += subset[a]
                    else:
                        break
            if commonString == "":
                return ""
            
            if len(outputString) > len(commonString):
                outputString = commonString
            
        return outputString