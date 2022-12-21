# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        
        
#         KthSml = None
        
#         def CheckN(node):
#             nonlocal k
#             nonlocal KthSml
#             if not node:
#                 return
#             CheckN(node.left)
            
#             k -= 1
#             if k == 0:
#                 KthSml = node
#             CheckN(node.right)
            
#         CheckN(root)
#         return KthSml.val
    
        
        
#         kthMax = None
#         def CheckNode(node):
#             nonlocal k
#             nonlocal kthMax
#             if node.left:
#                 CheckNode(node.left)
    
#             k = k -1
#             if k == 0:
#                 kthMax = node.val
#             if node.right:
#                 CheckNode(node.right)
                
#         CheckNode(root)       
        
#         return kthMax
        