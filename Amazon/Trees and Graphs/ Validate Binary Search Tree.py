# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # def traverse(node, left=float('-inf'), right=float('inf')):
        #     if node is None: return True
        #     if node.val <= left or node.val >= right: return False
        #     if not traverse(node.left, left, node.val): return False
        #     if not traverse(node.right, node.val, right):return False
        #     return True
        left=float('-inf')
        right=float('inf')
        stack = [(root, left, right)]
        while stack:
            node, left, right = stack.pop()
            if not node: continue
            if node.val <= left or node.val >= right: return False
            stack.append((node.left, left, node.val))
            stack.append((node.right, node.val, right))
        return True
        
    