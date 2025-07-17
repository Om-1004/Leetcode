class Solution:
    def longestPalindrome(self, s: str) -> int:
        obj = {}
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            if s[i] not in obj:
                obj[s[i]] = 1
            else:
                obj[s[i]] += 1
        
        length = 0
        hasOddValue = False

        for j in obj.values():
            if j % 2 != 0:
                hasOddValue = True
                length = length + j - 1
            else:
                length += j
        
        if hasOddValue == True:
            length += 1

        return length
        