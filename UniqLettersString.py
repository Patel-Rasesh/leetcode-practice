class Solution:
    def uniqLettersString(self, s):
        output = [[]]
        s = list(s)
        result = 0
        for charac in s:
            for curr in range(len(output)):
                for i, ch in enumerate(output[curr]):
                    if ch == charac:
                #if charac in output[curr]:
                       output[curr].pop(i)
                    output += output[curr]
                    continue
                output += [output[curr] + [charac]]
            # for uniqueCharac in temp:
            #     if temp.count(uniqueCharac) == 1:
            #         result += 1
                #print(uniqueCharac)
            # output += temp
        return output

obj = Solution()
s = "ABA"
print(obj.uniqLettersString(s))