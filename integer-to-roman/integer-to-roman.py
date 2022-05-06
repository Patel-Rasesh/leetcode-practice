class Solution(object):
    RomanDict = {}
    RomanDict[0] = ''
    RomanDict[1] = 'I'
    RomanDict[2] = 'II'
    RomanDict[3] = 'III'
    RomanDict[4] = 'IV'
    RomanDict[5] = 'V'
    RomanDict[6] = 'VI'
    RomanDict[7] = 'VII'
    RomanDict[8] = 'VIII'
    RomanDict[9] = 'IX'
    RomanDict[10] = 'X'
    RomanDict[50] = 'L'
    RomanDict[100] = 'C'
    RomanDict[500] = 'D'
    RomanDict[1000] = 'M'
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ""
        return self.findRoman(num, output)
    def findRoman(self, num, output):
        if num // 1000:
        # if number%5000 > 1900:
        #     output += self.RomanDict[1000]
        #     output += self.RomanDict[100]
        #     return self.findRoman(number-1900, output)
        # else:
            output += self.RomanDict[1000]
            return self.findRoman(num-1000, output)
        if num // 500:
            if num%1000 >= 900:
                output += self.RomanDict[100]
                output += self.RomanDict[1000]
                return self.findRoman(num-900, output)
            else:
                output += self.RomanDict[500]
                return self.findRoman(num-500, output)
        if num // 100:
            if num%500 >= 400:
                output += self.RomanDict[100]
                output += self.RomanDict[500]
                return self.findRoman(num-400, output)
            else:
                output += self.RomanDict[100]
                return self.findRoman(num-100, output)
        if num // 50:
            if num%100 >= 90:
                output += self.RomanDict[10]
                output += self.RomanDict[100]
                return self.findRoman(num-90, output)
            else:
                output += self.RomanDict[50]
                return self.findRoman(num-50, output)
        if num // 10:
            if num%50 >= 40:
                output += self.RomanDict[10]
                output += self.RomanDict[50]
                return self.findRoman(num-40, output)
            else:
                output += self.RomanDict[10]
                return self.findRoman(num-10, output)
        output += self.RomanDict[num]
        return output
        