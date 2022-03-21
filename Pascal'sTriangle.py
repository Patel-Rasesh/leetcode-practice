class Solution(object):
    def generate(self, numRows):
        output = [[1]]
        for numberOfRows in range(numRows-1):
            tempOutput = output[numberOfRows]
            temp = []
            temp.append(tempOutput[0])
            for subArray in range(len(tempOutput)-1):
                temp.append(tempOutput[subArray] + tempOutput[subArray+1])
            temp.append(tempOutput[-1])
            output.append(temp)
        return output[numRows-1]
        

obj = Solution()
print(obj.generate(5))