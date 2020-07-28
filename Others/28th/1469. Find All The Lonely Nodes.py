# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.arr = []
        
        def dfs(node: TreeNode):
            if node.left and not node.right:
                self.arr.append(node.left.val)
            if not node.left and node.right:
                self.arr.append(node.right.val)
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
        dfs(root)
        return self.arr