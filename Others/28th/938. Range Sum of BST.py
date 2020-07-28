# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None: return 0
        if root.val > R: return self.rangeSumBST(root.left, L, R)
        if root.val < L: return self.rangeSumBST(root.right, L, R)
        return root.val + self.rangeSumBST(root.left, L ,R) + self.rangeSumBST(root.right, L ,R)
    
#         def dfs(node):
#             if node:
#                 if L <= node.val <= R:
#                     self.ans += node.val
#                 if L < node.val:
#                     dfs(node.left)
#                 if R > node.val:
#                     dfs(node.right)
        
#         self.ans = 0
#         dfs(root)
#         return self.ans
                