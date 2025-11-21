class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(1, len(nums)):
            res[i] = pre * nums[i - 1]
            pre *= nums[i-1]
        
        post = 1
        for j in range(len(nums) - 2, -1, -1):
            res[j] = res[j] * post * nums[j+1]
            post *= nums[j+1]

        return res


"""

Pre = 1

[1, 2, 3, 4]
          _
[1, 1, 2, 1]

[1, 1, ]

"""
        