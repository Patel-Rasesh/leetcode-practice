class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        iterator = 0
        outputString = ""
        index = 0
        # Sort sources and targets based on indices
        masterParams = sorted(zip(indices, sources, targets))
        #return sorted(zip(indices, sources, targets))
        sortedIndices, sortedSources, sortedTargets = [], [], []
        for i in range(len(masterParams)):
            sortedIndices.append(masterParams[i][0])
            sortedSources.append(masterParams[i][1])
            sortedTargets.append(masterParams[i][2])

        #return (sortedIndices, sortedSources, sortedTargets)
        while index < (len(s)):
            if index in sortedIndices:
                if sortedSources[iterator] == s[index:index+len(sortedSources[iterator])]:
                    outputString += sortedTargets[iterator]
                    index += len(sortedSources[iterator])
                else:
                    outputString += s[index]
                    index += 1
                iterator += 1
            else:
                outputString += s[index]
                index += 1
        return outputString

obj = Solution()
s="mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr"
indices = [46,29,2,44,31,26,42,9,38,23,36,12,16,7,33,18]
sources = ["rym","kv","nbzxu","vx","js","tp","tc","jta","zqm","ya","uz","avm","tz","wn","yv","ird"]
targets = ["gfhc","uq","dntkw","wql","s","dmp","jqi","fp","hs","aqz","ix","jag","n","l","y","zww"]
print(obj.findReplaceString(s, indices, sources, targets))