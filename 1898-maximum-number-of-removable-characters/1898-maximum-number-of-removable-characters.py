class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubSeq(s, subs):
            i1 = 0
            i2 = 0
            while i1 < len(s) and i2 < len(subs):
                if i1 in removed or s[i1] != subs[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            return i2 == len(subs)
            
        
        
        l = 0
        r = len(removable)
        res = 0
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[:m])
            if isSubSeq(s, p):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
        