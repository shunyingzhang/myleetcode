class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False
            i = t.index(c)
            t = t[i + 1:]
        return True
        