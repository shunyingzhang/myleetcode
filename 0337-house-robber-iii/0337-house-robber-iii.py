# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            return [node.val + left[1] + right[1], max(left) + max(right)]
        return max(dfs(root))
        
        
#         def robber(node):
#             if not node:
#                 return 0
            
#             if not node.left and not node.right:
#                 return node.val
            
#             if node.left and node.right:
#                 return (node.val + robber(node.left.left) + robber(node.left.right) + robber(node.right.right) + robber(node.right.left))
#             if node.left and not node.right:
#                 return (node.val + robber(node.left.left) + robber(node.left.right))
#             if not node.left and node.right:
#                 return (node.val + robber(node.right.right) + robber(node.right.left))
        
#         return max(robber(root), robber(root.left) + robber(root.right))