class Solution:
    def reverse(self, x: int) -> int:

        
        isNeg = False
        if x < 0:
            isNeg = True
        
        x = abs(x)
        
        strNum = str(x)
        reversedStrNum = strNum[::-1]
        reversedBack = int(reversedStrNum)

    

        if isNeg:
            reversedBack *= -1


        if reversedBack > 2 ** 31 - 1 or reversedBack < -2 ** 31:
            return 0

        return reversedBack

