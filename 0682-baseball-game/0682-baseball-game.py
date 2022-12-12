class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        rcd = []
        for op in operations:
            if op == "+":
                tmp = rcd[-1] + rcd[-2]
                rcd.append(rcd[-1] + rcd[-2])
                res += tmp
            elif op == "D":
                tmp = rcd[-1] * 2
                rcd.append(rcd[-1] * 2)
                res += tmp
            elif op == "C":
                tmp = rcd.pop()
                res -= tmp
            else:
                rcd.append(int(op))
                res += int(op)
        return res
                
        