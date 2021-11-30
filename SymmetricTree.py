# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.mirror(root.left, root.right)

    def mirror(self, t1, t2):
        if t1 and t2:
            return t1.val == t2.val and self.mirror(
                t1.left, t2.right) and self.mirror(t1.right, t2.left)
        return False