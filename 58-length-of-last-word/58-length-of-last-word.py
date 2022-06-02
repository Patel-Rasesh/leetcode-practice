class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengthOfLastWord = 0
        # 1. Start iterating in a loop in reverse
        for charac in range(len(s)-1, -1, -1):
            # 2. Continue loop until a character is encountered
            
            if s[charac] == ' ':
                if lengthOfLastWord != 0:
                    return lengthOfLastWord
                continue
            # 3. Count until next space is encountered
            lengthOfLastWord += 1
        
        return lengthOfLastWord