def solution(A):
    tArrLength = len(A)
    tBit = [0 for tIterator in range(32)]
    for tIterator in range(tArrLength):
        x = 31
        while(A[tIterator] > 0):
            if (A[tIterator] & 1 == 1):
                tBit[x] += 1
            A[tIterator] = A[tIterator] >> 1 
            x -= 1
    print(max(tBit))
solution([13, 7, 2, 8, 3])
