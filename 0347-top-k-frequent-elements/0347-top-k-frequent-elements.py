from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        res = [0] * k
        frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

        i = 0
        for key, value in frequency.items():
            if i < k:
                res[i] = key
                i += 1
        
        return res
            
