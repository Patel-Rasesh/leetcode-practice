inputString = "cdd"
    
tempArray = []
outputArray = []
if(len(inputString) == 1):
    tempArray.append(input)
    outputArray.append(tempArray)
else:
    for i in range(len(inputString)-1):
        for runner in range(len(inputString)):
        #for runner in range(len(input)-i):
            temp = inputString[runner:runner+i+1]
            if(temp == temp[::-1]):
                tempArray.append(temp)
        size = 0
        
        tempOutputArray = []
        for item in tempArray:
            size += len(item)
            if(size <= len(inputString)):
                tempOutputArray.append(item)
                if(size == len(inputString)):
                    outputArray.append(tempOutputArray)
        tempArray = []
        runner = 0
print(outputArray)