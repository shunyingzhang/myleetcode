# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        GN = 0
        
        def findGoodN(p, value):
            nonlocal GN
            if p.val >= value:
                value = p.val
                GN += 1
            if p.left:
                findGoodN(p.left, value)
            if p.right:
                findGoodN(p.right, value)
            return GN        
        
        res_val = root.val
        
        left = 0
        right = 0
        
        if root.left:
            GN = findGoodN(root.left, res_val)
        if root.right:
            GN = findGoodN(root.right, res_val)
            
        
        return 1 + GN