class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0

        while l < len(nums):
            r = l + 1
            if nums[l] == 0:
                while r < len(nums) and nums[r] == 0:
                    r += 1
                
                if r == len(nums):
                    return

                nums[l], nums[r] = nums[r], nums[l]
                r += 1
            l += 1

"""

0 1 0 3 12
L R

1 3 0 0 12
    L   R

"""