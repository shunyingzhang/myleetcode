class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        total = 0
        res = 0
        
        for r in range(len(arr)):
            total += arr[r]
            
            if r >= k - 1:
                if total / k >= threshold:
                    res += 1
                
                total -= arr[r - k + 1]
            
        return res
            
                
        