class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hash_map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for bracket in s:
            if bracket in hash_map.values():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                openingBracket = stack.pop()
                if hash_map[bracket] != openingBracket:
                    return False
        return len(stack) == 0

