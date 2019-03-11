# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root == None:
            return result
        if root.left != None:
            result += (self.inorderTraversal(root.left))
        result.append(root.val)
        if root.right != None:
            result += (self.inorderTraversal(root.right))
        return result
