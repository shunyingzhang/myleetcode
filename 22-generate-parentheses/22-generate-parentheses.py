class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        track = []
        res = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(track))
                return
            if openN < n:
                track.append("(")
                backtrack(openN + 1, closeN)
                track.pop()
            if closeN < openN:
                track.append(")")
                backtrack(openN, closeN + 1)
                track.pop()
        backtrack(0, 0)
        return res