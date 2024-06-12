class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            longerString = a
            shorterString = b
        else: 
            longerString = b
            shorterString = a
        
        while len(shorterString)!=len(longerString):
            shorterString = "0"+ shorterString

        i = len(longerString) -1
        carryBit = 0
        sumBit = 0
        result = ""
        while i >= 0:
            if (carryBit + int(shorterString[i]) + int(longerString[i]) == 3):
                carryBit = 1
                result = "1" + result

            elif (carryBit + int(shorterString[i]) + int(longerString[i]) == 2):
                carryBit = 1
                result = "0" + result
            
            else:
                result = str(int(shorterString[i])+int(longerString[i])+carryBit) + result
                carryBit=0
            
            i-=1

        if carryBit == 1:
            result = "1" + result

        return result


        