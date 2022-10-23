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
        
        def findGoodN(p, value, GN):
            if p.val >= value:
                value = p.val
                GN += 1
            if p.left:
                GN = findGoodN(p.left, value, GN)[1]
            if p.right:
                GN = findGoodN(p.right, value, GN)[1]
            return [value, GN]
        
        GN = 0
        
        res_val = root.val
        
        left = 0
        right = 0
        
        if root.left:
            left = findGoodN(root.left, res_val, GN)[1]
        if root.right:
            right = findGoodN(root.right, res_val, GN)[1]
            
        
        return 1 + left + right