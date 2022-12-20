# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def findH(node):
            if not node:
                return [True, 0]
            left = findH(node.left)
            right = findH(node.right)
            bal = ( left[0] and right[0] 
                   and abs(left[1] - right[1]) <= 1)
            return [bal, 1 + max(left[1], right[1])]
        return findH(root)[0]
        
        
#         def findHeight(root):
#             if not root:
#                 return [True, 0]
            
#             left = findHeight(root.left)
#             right = findHeight(root.right)

#             balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
#             return [balanced, 1 + max(left[1], right[1])]
        
#         return findHeight(root)[0]
        