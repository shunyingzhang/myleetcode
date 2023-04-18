class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pmap = {}
        smap = {}
        res = []
        
        for c in p:
            pmap[c] = 1 + pmap.get(c, 0)
        
        for i, c in enumerate(s):
            smap[c] = 1 + smap.get(c, 0)
            
            if i >= len(p) - 1:
                if smap == pmap:
                    res.append(i - len(p) + 1)
            
            
                smap[s[i - len(p) + 1]] -= 1
                if not smap[s[i - len(p) + 1]]:
                    del smap[s[i - len(p) + 1]]
        
        return res
        