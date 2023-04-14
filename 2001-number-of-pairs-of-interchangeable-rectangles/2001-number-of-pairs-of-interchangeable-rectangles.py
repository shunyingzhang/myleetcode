class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hmap = {}
        
        for w, h in rectangles:
            hmap[w / h] = 1 + hmap.get(w / h, 0)
        
        res = 0
        
        for c in hmap.values():
            if c > 1:
                res += c * (c - 1) // 2
        
        return res
        