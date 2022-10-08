class Solution:
    def isValid(self, s: str) -> bool:
        OpenClose = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for c in s:
            if c in OpenClose:
                if stack and stack[-1] == OpenClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True
        