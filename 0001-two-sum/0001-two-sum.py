class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i in range(len(nums)):
            complement = target - nums[i] 

            if complement in dictt:
                return [dictt[complement], i]
            else:
                dictt[nums[i]] = i


