sample = [[".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."]]

          [[".",".",".",".","5",".",".","1","."],
           [".","4",".","3",".",".",".",".","."],
           [".",".",".",".",".","3",".",".","1"],
           ["8",".",".",".",".",".",".","2","."],
           [".",".","2",".","7",".",".",".","."],
           [".","1","5",".",".",".",".",".","."],
           [".",".",".",".",".","2",".",".","."],
           [".","2",".","9",".",".",".",".","."],
           [".",".","4",".",".",".",".",".","."]]
flag = True
countDotsRows = 0
countDotsCols = 0
for row in range(len(sample)):
    for column in range(len(sample[row])):
        for neighborH in range(column+1, len(sample[row])):
            if (sample[row][column] != ".") and (sample[row][column] == sample[row][neighborH]):
                print("invalid at ", (row, neighborH))
            elif (sample[row][column] == ".") and (sample[row][column] == sample[row][neighborH]):
                countDotsRows += 1
        if countDotsRows == len(sample[row]) - 1:
            print("invalid because - ", countDotsRows)
        countDotsRows = 0
        for neighborV in range(row+1, len(sample)):
            if (sample[row][column] != ".") and (sample[row][column] == sample[neighborV][column]):
                print("invalid at ", (neighborV, column))
            elif (sample[row][column] == ".") and (sample[row][column] == sample[neighborV][column]):
                countDotsCols += 1
        if countDotsCols == len(sample) - 1:
            print("invalid because - ", countDotsCols)
        countDotsCols = 0
    # if flag == True:
    #     print("invalid")