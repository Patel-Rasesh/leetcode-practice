from collections import defaultdict

inputString = "abcabcbb"
inputCharac = list(inputString)

score = defaultdict(int)
result = []
count = 0

runner = 0
while(runner < len(inputCharac)):
    for i, character in enumerate(inputCharac[runner:]):
        if(score[character] == 1):
            result.append(count)
            count = 0
            runner += 1
            # Reset the dictionary too
            score.clear()
            break
        score[character] += 1
        count += 1
    
print("Length of the maximum Substring is, ", max(result))