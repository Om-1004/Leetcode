class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == 'D':
                lastVal = int(stack[-1]) * 2
                stack.append(lastVal)
            
            elif operation == 'C':
                stack.pop()

            elif operation == '+':
                lastVal, secondLastVal = stack[-1], stack[-2]
                stack.append(int(lastVal) + int(secondLastVal))
            
            else:
                stack.append(int(operation))

        return sum(stack)
        
"""

"5","-2","4","C","D","9","+","+"

[5 -2, -4, 9, 5, 14 ]

"""

