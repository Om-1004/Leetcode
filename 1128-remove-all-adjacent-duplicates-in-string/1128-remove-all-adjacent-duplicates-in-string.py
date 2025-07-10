class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        if len(s) == 0:
            return ""
        
        stack = [s[0]]

        for i in range(1, len(s)):
            if stack:
                if s[i] != stack[-1]:
                    stack.append(s[i])
                else:
                    stack.pop()
            else:
                stack.append(s[i])
            
        return ''.join(stack)
