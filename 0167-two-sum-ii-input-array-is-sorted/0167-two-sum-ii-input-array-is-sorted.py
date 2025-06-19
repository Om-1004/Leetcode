class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            left, right = numbers[l], numbers[r]
            if left + right > target:
                r -= 1
            
            if left + right < target:
                l += 1

            if left + right == target:
                return [l+1, r+1]
            
  
"""
2 7 11 15 
l.   r

left = 2
right = 15
"""