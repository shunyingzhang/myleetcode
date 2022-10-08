class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for n in tokens:
            if n == '+':
                res.append(res.pop() + res.pop())
            elif n == '-':
                a = res.pop()
                b = res.pop()
                res.append(b - a)
            elif n == '*':
                res.append(res.pop() * res.pop())
            elif n == '/':
                a = res.pop()
                b = res.pop()
                res.append(int(b / a))
            else:
                res.append(int(n))
            
        return res[0]
        