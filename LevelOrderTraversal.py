# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        currLevel = [root]
        nextLevel = []
        levelList = []
        result = []
        while currLevel:
            for root in currLevel:
                levelList.append(root.val)
                if root.left:
                    nextLevel.append(root.left)
                if root.right:
                    nextLevel.append(root.right)
            result.append(levelList)
            levelList = []
            currLevel = nextLevel
            nextLevel = []
        return result