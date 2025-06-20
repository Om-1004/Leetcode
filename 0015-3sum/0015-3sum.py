class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        l, r = 0, len(arr) - 1
        mySet = set()
        while l < r:
            mover = l + 1
            while mover < r:
                left, middle, right = arr[l], arr[mover], arr[r]
                currentSum = left + middle + right

                if currentSum < 0:
                    mover += 1

                elif currentSum > 0:
                    r -= 1

                else:
                    if (left, middle, right) not in mySet:
                       mySet.add((left, middle, right))
                    r -= 1
            
            l += 1
            r = len(arr) - 1
            
        return list(mySet)
"""

-1 0 1 2 -1 -4

-4 -1 -1 0 1 2
       L M R



"""