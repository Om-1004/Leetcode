class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """



        l, r = 0, 1

        while l < len(nums):
            if nums[l] == 0:
                while r < len(nums) and nums[r] == 0:
                    r += 1
                if r < len(nums):
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                l += 1
                r += 1

"""

    L   R
1,3,12,0,0

"""