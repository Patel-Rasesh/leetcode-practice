class Solution(object):
    def permutation(self, index, tempComb, digits, phoneBookDict, combination):
        '''
        Base condition - when length of temporary combination and digits match
        '''
        if(len(tempComb) == len(digits)):
            combination.append("". join(tempComb))
            return
        # Typecasting is required as phone book dictionary has integer keys
        for alpha in phoneBookDict[int(digits[index])]:
            tempComb.append(alpha)
            self.permutation(index+1, tempComb, digits, phoneBookDict, combination)

            # Need to remove the latest alphabet added to temporary combination
            # Before proceeding to the next element of latest for loop
            tempComb.pop()

        return combination

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phoneBookDict = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'],
                     5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'], 7 : ['p', 'q', 'r', 's'], 
                     8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z']}
        digits = list(digits)
        combinationOutput = self.permutation(0, [], digits, phoneBookDict, [])
        return combinationOutput