class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                elif abs(a) < abs(stack[-1]):
                    a = 0
                else:
                    stack.pop()
                    a = 0
            if a != 0:
                stack.append(a)
        return stack
                
            
        