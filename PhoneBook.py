class PhoneBook:

    def permutation(self, index, tempComb, digits, phoneBookDict, combination):
        if(len(tempComb) == len(digits)):
            combination.append("". join(tempComb))
            return
        for alpha in phoneBookDict[int(digits[index])]:
            tempComb.append(alpha)
            self.permutation(index+1, tempComb, digits, phoneBookDict, combination)
            tempComb.pop()
        
        return combination

    def letterCombinations(self):
        phoneBookDict = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'],
                     5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'], 7 : ['p', 'q', 'r', 's'], 
                     8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z']}
        digits = "23"
        digits = list(digits)

        combinationOutput = self.permutation(0, [], digits, phoneBookDict, [])
        print(combinationOutput)
    
obj = PhoneBook()
obj.letterCombinations()