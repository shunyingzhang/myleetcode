# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(node, num):
            num += node.val
            if not node.left and not node.right:
                if num == targetSum:
                    return True
                else:
                    return False
            if node.left and not node.right:
                return pathSum(node.left, num)
            elif node.right and not node.left:
                return pathSum(node.right, num)
            else:
                return pathSum(node.left, num) or pathSum(node.right, num)
        if not root:
            return False
        return pathSum(root, 0)
        