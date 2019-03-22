# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            if abs(self.dfs(root.right) - self.dfs(root.left)) > 1:
                return False
            else:
                return True

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1
        return max(left, right) + 1
