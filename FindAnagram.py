class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []

        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        output = []
        # sliding window on the string s
        for i in range(len(s)):
            # add one more letter 
            # on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter 
            # from the left side of the window
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - len(p) + 1)
        
        return output

s = "cbaebabacd"
p = "abc"
obj = Solution()
print(obj.findAnagrams(s, p))
