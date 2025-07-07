class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        windowStart, currCount, max_length = 0, 0, 0
        dictt = dict()
        
        for windowEnd in range(len(fruits)):
            dictt[fruits[windowEnd]] = 1 + dictt.get(fruits[windowEnd], 0)
            currCount = currCount + 1 if len(dictt) <= 2 else currCount
            
            if len(dictt) > 2:
                max_length = max(max_length, currCount)
                while dictt[fruits[windowStart]] > 0:
                    dictt[fruits[windowStart]] = dictt.get(fruits[windowStart]) - 1
                    if dictt[fruits[windowStart]] == 0:
                        dictt.pop(fruits[windowStart])
                        windowStart += 1

                        break
                    windowStart += 1
                currCount = len(fruits[windowStart : windowEnd + 1])
        return max(max_length, currCount)
