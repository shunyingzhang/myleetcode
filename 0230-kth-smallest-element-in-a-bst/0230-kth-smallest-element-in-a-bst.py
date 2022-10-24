# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthMax = None
        def CheckNode(node):
            nonlocal k
            nonlocal kthMax
            if node.left:
                CheckNode(node.left)
    
            k = k -1
            if k == 0:
                kthMax = node.val
            if node.right:
                CheckNode(node.right)
                
        CheckNode(root)       
        
        return kthMax
        