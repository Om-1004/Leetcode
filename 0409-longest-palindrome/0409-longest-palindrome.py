class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictt = dict()

        for letter in s:
            dictt[letter] = 1 + dictt.get(letter, 0)
        
        count = 0
        flag = False

        for value in dictt.values():
            if value % 2 == 0:
                count += value
            else:
                counter = value // 2
                count += (counter * 2)
                flag = True

        return count + 1 if flag else count


            
