# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def checkN(node, left, right):
            if not node:
                return True
        
            if not (node.val > left and node.val < right):
                return False
            return checkN(node.left, left, node.val) and checkN(node.right, node.val, right)
        
        return checkN(root, float("-inf"), float("inf"))
        
#         if not root:
#             return True
        
#         def CheckNode(node, left, right):
#             if not node:
#                 return True
            
#             if not (node.val > left and node.val < right):
#                 return False
            
#             return (CheckNode(node.left, left, node.val) and CheckNode(node.right, node.val, right))
        
#         return CheckNode(root, float("-inf"), float("inf"))
            
        