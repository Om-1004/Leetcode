class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {0: 0, 1: 1, 2: 2}

        if n <= 2:
            return memo[n]

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-2) + f(x-1)
                return memo[x]

        return f(n)        
"""

2:
1 + 1
2 

3 
2 + 1
1 + 2
1 + 1 + 1

4
3 + 1
2 + 2
1 + 3
1 + 1 + 2
2 + 1 + 1

"""