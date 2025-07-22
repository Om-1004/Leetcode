class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        left = []
        right = []
        while num1:
            left.append(int(num1[0]) * (10 ** (len(num1) - 1)))
            num1 = num1[1: ]

        while num2:
            right.append(int(num2[0]) * (10 ** (len(num2) - 1)))
            num2 = num2[1: ]
        
        sum = 0
        for i in range(len(left)):
            for j in range(len(right)):
                sum += left[i] * right[j]

        return str(sum)

"""

123 
[ ]

while num:
    res.append(int(num1) * (10 * len(num1))
    num1 = num1[1: ]


[100, 20, 3], [400, 50, 6]

"""