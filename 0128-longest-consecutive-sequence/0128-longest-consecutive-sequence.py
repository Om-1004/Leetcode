class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        maxLen = 0

        for num in values:
            if (num - 1) not in values:
                length = 1
                while (num + length) in values:
                    length += 1
                maxLen = max(length, maxLen)
        
        return maxLen
