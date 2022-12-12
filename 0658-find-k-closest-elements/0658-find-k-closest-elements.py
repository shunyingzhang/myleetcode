class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        p1 = 0
        gap = arr[len(arr) - 1]
        
        for i, a in enumerate(arr):
            if abs(a - x) < gap:
                gap = abs(a - x)
                p1 = i
        
        p2 = p1
        while p1 >= 0 and p2 < len(arr) and k - 1 > 0:
            if p1 > 0 and p2 < len(arr) - 1:
                if abs(arr[p1 - 1] - x) <= abs(arr[p2 + 1] - x):
                    p1 -= 1
                else:
                    p2 += 1
            elif p1 == 0:
                p2 += 1
            else:
                p1 -= 1
            k -= 1
        
            
            
        return arr[p1: p2 + 1]    
            
        