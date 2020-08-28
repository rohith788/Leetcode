# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        stem = defaultdict(list)
        def traverse(node, lev):
            if node:
                stem[lev].append(node.val)
                traverse(node.left, lev+1)
                traverse(node.right, lev+1)
        traverse(root, 0)
        arr = []
        for i in stem.keys():
            arr.append(stem[i][-1])
        return arr