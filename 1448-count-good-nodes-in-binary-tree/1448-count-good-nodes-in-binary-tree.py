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
        gn = 0
        
        def findG(node, ref):
            nonlocal gn
            if not node:
                return 0
            gn = findG(node.left, max(ref, node.val))
            gn += findG(node.right, max(ref, node.val))
            
            if node.val >= ref:
                return 1 + gn
            else:
                return gn
        
        return findG(root, root.val)
        
        
        
        
        
#         if not root:
#             return 0
        
#         GN = 0
        
#         def findGoodN(p, value):
#             nonlocal GN
#             if p.val >= value:
#                 value = p.val
#                 GN += 1
#             if p.left:
#                 findGoodN(p.left, value)
#             if p.right:
#                 findGoodN(p.right, value)
#             return GN        
        
#         res_val = root.val
        
#         left = 0
#         right = 0
        
#         if root.left:
#             GN = findGoodN(root.left, res_val)
#         if root.right:
#             GN = findGoodN(root.right, res_val)
            
        
#         return 1 + GN