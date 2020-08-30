# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        stack = []
        node = root
        while node or stack:
            if not node:
                node = stack.pop()
            else:
                while node.right:
                    stack.append(node)
                    node = node.right
            node.val += total
            total = node.val
            node = node.left
        return root