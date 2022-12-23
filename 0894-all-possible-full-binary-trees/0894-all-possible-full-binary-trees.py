# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            res = []
            for l in range(1, n, 2):
                r = n - l - 1
                lTrees = backtrack(l)
                rTrees = backtrack(r)
                for lTree in lTrees:
                    for rTree in rTrees:
                        node = TreeNode(0)
                        node.left = lTree
                        node.right = rTree
                        res.append(node)
            return res
        return backtrack(n)
                
                
                
        