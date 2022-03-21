a = 8
#10000010001
b = bin(a)
def solution(N):
    tempBin = bin(N)
    #print(tempBin)
    countZero = 0
    flag = False
    zeroArray = [0]
    for i in range(2, len(tempBin)):
        if(tempBin[i] == '1'):
            if countZero > 0:
                zeroArray.append(countZero)
                countZero = 0
            flag = True
            continue
        if(tempBin[i] == '0' and flag == True):
            countZero += 1
    return max(zeroArray)

print(solution(32))