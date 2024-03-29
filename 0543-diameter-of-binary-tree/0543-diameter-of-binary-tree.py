# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def findH(node):
            nonlocal res
            if not node:
                return 0
            left = findH(node.left)
            right = findH(node.right)
            
            res = max(res, left + right)
            return 1 + max(left, right)
        findH(root)
        
        return res
        
        
        
        
#         res = 0
        
#         def findHeight(root):
#             nonlocal res
#             if not root:
#                 return 0
            
#             left = findHeight(root.left)
#             right = findHeight(root.right)
#             res = max(res, left + right)
            
#             return 1 + max(left, right)
        
#         findHeight(root)
        
#         return res
        