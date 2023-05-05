class Solution:
    def isValid(self, s: str) -> bool:
        openclose = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for c in s:
            if c in openclose:
                if stack and stack[-1] == openclose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        return True
        
        
        
#         OpenClose = {')': '(', ']': '[', '}': '{'}
#         stack = []
        
#         for c in s:
#             if c in OpenClose:
#                 if stack and stack[-1] == OpenClose[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
#         if stack:
#             return False
#         else:
#             return True
        