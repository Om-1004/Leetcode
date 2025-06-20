class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        my_set = set(['b', 'a', 'l', 'o', 'n'])

        for i in range(len(text)):
            if text[i] in my_set:
                hash_map[text[i]] += 1

        
        minVal = min(hash_map.values())
        lCount = hash_map['l'] // 2
        oCount = hash_map['o'] // 2

        if minVal <= lCount and minVal <= oCount:
            return minVal
        else:
            return min(lCount, oCount, minVal)

