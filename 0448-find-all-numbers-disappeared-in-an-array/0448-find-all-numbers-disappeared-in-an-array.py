class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        mySet = set(nums)
        arr = []
        for i in range(1, len(nums)+1):
            if i not in mySet:
                arr.append(i)
        return arr