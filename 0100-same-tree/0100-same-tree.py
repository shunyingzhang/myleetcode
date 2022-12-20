# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        q1 = deque([p])
        q2 = deque([q])
        
        while q1 or q2:
            if len(q1) != len(q2):
                return False
            for i in range(len(q1)):
                n1 = q1.popleft()
                n2 = q2.popleft()
                if n1.val != n2.val:
                    return False
                if (n1.left and not n2.left) or (not n1.left and n2.left):
                    return False
                if n1.left:
                    q1.append(n1.left)
                    q2.append(n2.left)
                if (n1.right and not n2.right) or (not n1.right and n2.right):
                    return False
                if n1.right:
                    q1.append(n1.right)
                    q2.append(n2.right)
                    
        return True
        
        
        
        
#         if not p and not q:
#             return True
#         if not p or not q or p.val != q.val:
#             return False
        
#         return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        