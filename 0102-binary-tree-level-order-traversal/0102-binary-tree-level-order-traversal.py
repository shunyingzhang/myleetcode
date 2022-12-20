# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        
        while q:
            trav = []
            for i in range(len(q)):
                node = q.popleft()
                trav.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(trav)
        return res
        
        
        
#         res = []
#         if not root:
#             return res
        
#         q = deque([root])
#         while q:
#             value = []
#             for j in range(len(q)):
#                 node = q.popleft()
#                 value.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             res.append(value)
#         return res
       
        