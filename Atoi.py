#s = "4193 with words"
s = "words and 987"

flag = True
filteredNumber = ''
for charac in s:
    if charac == ' ':
        continue
    if charac == '-':
        flag = False
    if ord(charac) >= 48 and ord(charac) <= 57:
        filteredNumber += charac

print(filteredNumber)
numDict = {}
numDict[ord('0')] = 0
numDict[ord('1')] = 1
numDict[ord('2')] = 2
numDict[ord('3')] = 3
numDict[ord('4')] = 4
numDict[ord('5')] = 5
numDict[ord('6')] = 6
numDict[ord('7')] = 7
numDict[ord('8')] = 8
numDict[ord('9')] = 9

digit = 0
for number in range(len(filteredNumber)):
    digit = digit*10 + numDict[ord(filteredNumber[number])]

if flag == False:
    digit = digit * -1

print(digit, type(digit))