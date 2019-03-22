"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def post_order(self, root, res: list) -> list[int]:
        if not root:
            for n in root.children:
                self.post_order(n, res)
            res.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.post_order(root, res)
        return res
