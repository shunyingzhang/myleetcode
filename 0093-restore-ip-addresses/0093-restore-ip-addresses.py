class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        length = len(s)
        def dfs(s1, k, sub):
            nonlocal length
            if k == 4 and len(sub) == length + 4:
                res.append(sub[: -1])
                return
            
            if len(sub) == length + 4:
                return
            
            # if s1[0] == '0':
            #     return
            
            for i in range(3):
                if i < len(s1):
                    c = s1[: i + 1]
                    if (len(c) > 1 and c[0] == '0'
                        or int(c) > 255):
                        continue
                    dfs(s1[i + 1:], k + 1, sub + c + '.')
        
        dfs(s, 0, '')
        
        return res
                
        