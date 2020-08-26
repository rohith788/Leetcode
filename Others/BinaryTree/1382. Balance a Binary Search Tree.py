# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def dfs(node):
            if node:
                dfs(node.left)
                arr.append(node.val)
                dfs(node.right)
                
        dfs(root)
        
        def balance(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = balance(arr[:mid])
            root.right = balance(arr[mid+1:])
            return root
        
        return balance(arr)