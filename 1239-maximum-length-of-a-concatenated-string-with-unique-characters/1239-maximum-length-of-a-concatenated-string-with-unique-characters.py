class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = 0
        
        def ifunique(s1, s2):
            count = Counter(s1) + Counter(s2)
            if max(count.values()) > 1:
                return False
            else:
                return True
            
            
            
        def dfs(i, cur):
            nonlocal maxlen
            if i == len(arr):
                maxlen = max(maxlen, len(cur))
                return
            
            if ifunique(cur, arr[i]):
                dfs(i + 1, cur + arr[i])
            
            dfs(i + 1, cur)
        
        dfs(0, '')
        return maxlen
        