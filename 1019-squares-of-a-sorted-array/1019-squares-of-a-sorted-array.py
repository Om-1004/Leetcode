class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
 
        while l <= r:
            left = nums[l] ** 2
            right = nums[r] ** 2
            
            if right > left:
                res[r - l] = right
                r -= 1
            else:
                res[r - l] = left
                l += 1
        return res


            


"""

[-7,-3,2,3,11]
       L R


_ 8 9 49 121




-5 -3 -2 -1
    L     R

         25/
"""