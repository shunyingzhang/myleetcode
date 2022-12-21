class Solution:
    def numTrees(self, n: int) -> int:
        tnode = [1] * (n + 1)
        
        for nodes in range(2, n + 1):
            res = 0
            for i in range(1, nodes + 1):
                left = i - 1
                right = nodes - i 
                res += tnode[left] * tnode[right]
            tnode[nodes] = res
        return tnode[n]
        
            
        
        
        
#         hmap = {}
#         hmap[0] = 1
#         hmap[1] = 1
        
#         def numT(n):
#             res = 0
            
#             for i in range(1, n + 1):
#                 if i - 1 in hmap:
#                     left = hmap[i - 1]
#                 else:
#                     left = self.numTrees(i - 1)
#                     hmap[i - 1] = left
#                 if n - i in hmap:
#                     right = hmap[n - i]
#                 else:
#                     right = self.numTrees(n - i)
#                     hmap[n - i] = right
    
#                 res += left * right             
#             return res
#         return numT(n)
        