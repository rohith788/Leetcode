# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.traverse(root)
        
    def traverse(self, node, left=float('-inf'), right=float('inf')):
        if not node: return True
        print(node.val, left, right)
        if node.val <= left or node.val >= right: return False
        if not self.traverse(node.left, left, node.val): 
            return False
        if not self.traverse(node.right, node.val, right): 
            return False
        return True