from ast import Subscript


class Solution:
    def makeInteger(self, version):
        revisedVersion = 0
        for digit in version:
            revisedVersion = revisedVersion*10 + int(digit)
        return revisedVersion
    def compareVersion(self, version1, version2):
        
        substringVersion1 = version1.split('.')
        substringVersion2 = version2.split('.')

        print(substringVersion1)
        print(substringVersion2)

        # revisedVersion1 = self.makeInteger(substringVersion1)
        # revisedVersion2 = self.makeInteger(substringVersion2)


        # if revisedVersion2 > revisedVersion1:
        #     return -1
        # elif revisedVersion2 < revisedVersion1:
        #     return 1
        # return 0
        lengthofVersion1 = len(substringVersion1)
        lengthofVersion2 = len(substringVersion2)
        for version in range(min(lengthofVersion1, lengthofVersion2)):
            if version < lengthofVersion1:
                modifiedVersion1 = int(substringVersion1[version])
            elif version < lengthofVersion2:
                modifiedVersion2 = int(substringVersion2[version])
            if modifiedVersion2 != modifiedVersion1:
                if modifiedVersion2 > modifiedVersion1:
                    return -1
                else:
                    return 1
            return 0
            # if int(substringVersion1[version]) > int(substringVersion2[version]):
            #     return 1
            # elif int(substringVersion1[version]) < int(substringVersion2[version]):
            #     return -1

version1 = "1.0"
version2 = "1.0.0"
obj = Solution()
print(obj.compareVersion(version1, version2))
