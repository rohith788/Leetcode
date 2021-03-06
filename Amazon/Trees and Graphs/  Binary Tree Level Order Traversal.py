# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        arr = []
        def traverse(node, lev):
            if len(arr) == lev: arr.append([])
            arr[lev].append(node.val)
            if node.left: traverse(node.left, lev+1)
            if node.right: traverse(node.right, lev+1)
        traverse(root, 0)
        return arr