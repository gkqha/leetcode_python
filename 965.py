# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.tree(root, root.val)

    def tree(self, root, val):
        if root == None:
            return True
        else:
            if root.val != val:
                return False
            else:
                return self.tree(root.left, val) and self.tree(root.right, val)

