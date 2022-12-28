class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def ifunique(s1, s2):
            count = Counter(s1) + Counter(s2)
            if max(count.values()) > 1:
                return False
            else:
                return True
            
            
            
        def dfs(i, cur):
            # nonlocal maxlen
            if i == len(arr):
                # maxlen = max(maxlen, len(cur))
                return len(cur)
            len1 = 0
            if ifunique(cur, arr[i]):
                len1 = dfs(i + 1, cur + arr[i])
            
            len2 = dfs(i + 1, cur)
            return max(len1, len2)
        
        return dfs(0, '')
        