class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def findPar(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1 = findPar(n1)
            p2 = findPar(n2)
            if p1 == p2:
                return False
            
            if rank[p1] <= rank[p2]:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            else:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]
        