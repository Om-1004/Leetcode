class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(['*', '/', '+', '-'])
        total = 0

        for val in tokens:
            if val not in operands:
                stack.append(int(val))
            else:
                second, first = int(stack.pop()), int(stack.pop())
                if val == "*":
                    stack.append(first * second)
                elif val == '/':
                    stack.append(int(first / second))

                elif val == '+':
                    stack.append(first + second)
                else:
                    stack.append(first - second)
        
        return stack[0]


        