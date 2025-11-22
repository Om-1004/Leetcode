class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2

            if l == mid and nums[mid] < nums[r]:
                return nums[mid]
            
            elif l == mid and nums[mid] > nums[r]:
                return nums[r]

            elif nums[l] > nums[r]:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid
            
            else:
                r = mid
        return