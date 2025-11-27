class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, e = 0, len(nums) - 1

        r = 0
        while r <= e and l < e:
            if nums[r] == 0 or nums[r] == 2:
                if nums[r] == 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                
                if nums[r] == 2:
                    nums[r], nums[e] = nums[e], nums[r]
                    e -= 1

                if l > r:
                    r = l

            else:
                r += 1

"""
[2, 1]
 l
    r 
    e

"""