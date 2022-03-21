class Solution:
    def strstr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        pivot = 0
        requiredIndex = 0
        i = 0
        while(i < len(haystack)):
            if haystack[i] == needle[pivot]:
                if pivot == len(needle)-1:
                    return requiredIndex
                pivot+=1
            else:
                if pivot > 0:
                    i -= 2
                #i = i - pivot
                pivot = 0
                requiredIndex = i+1
            i+=1
        return -1

obj = Solution()
haystack, needle = "mississippi", "pi"
print(obj.strstr(haystack, needle))