class Solution:
    firstCharacCordinates = []
    def findinFour(self, board, row, col, word, storeLocation, index):
        # row - 1, row + 1, col - 1, col + 1
        #print("Printing neighbors for", board[row][col])
        if index >= len(word):
            return True
        if row-1 >= 0:
            if board[row-1][col] == word[index]:
                if [row-1, col] not in storeLocation:
                    storeLocation.append([row-1, col])
                    #print("Found at", (row-1, col))
                    index += 1
                    return self.findinFour(board, row-1, col, word, storeLocation, index)
        if col-1 >= 0:
            if board[row][col-1] == word[index]:
                if [row, col-1] not in storeLocation:
                    storeLocation.append([row, col-1])
                    #print("Found at", (row, col-1))
                    index += 1
                    return self.findinFour(board, row, col-1, word, storeLocation, index)
        if row+1 <= len(board):
            if board[row+1][col] == word[index]:
                if [row+1, col] not in storeLocation:
                    storeLocation.append([row+1, col])
                    #print("Found at", (row+1, col))
                    index += 1
                    return self.findinFour(board, row+1, col, word, storeLocation, index)
        if col+1 <= len(board):    
            if board[row][col+1] == word[index]: 
                if [row, col+1] not in storeLocation:
                    storeLocation.append([row, col+1])
                    #print("Found at", (row, col+1))
                    index += 1
                    return self.findinFour(board, row, col+1, word, storeLocation, index)
        if board[row][col] == word:
            if [row, col] not in storeLocation:
                storeLocation.append([row, col])
                index += 1
        return False
    def findFirst(self, board, charac):
        # This function returns an array of all the possible cordinates of
        # the first letter
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == charac:
                    self.firstCharacCordinates.append([row, col])
        #return self.firstCharacCordinates
    def exist(self, board, word):
        self.findFirst(board, word[0])
        print(self.firstCharacCordinates)
        flagArray = []
        for eachFinding in self.firstCharacCordinates:
            tempFlag = self.findinFour(board, eachFinding[0], eachFinding[1], word, [], 1)
            flagArray.append(tempFlag)
        for flag in flagArray:
            if flag == True:
                return True
        return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
#word = "ABCB"
object = Solution()
print(object.exist(board, word))