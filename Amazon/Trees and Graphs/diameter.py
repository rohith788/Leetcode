# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            if node is None:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            
            self.ans = max(self.ans, l+r+1)
            
            return max(l,r)+1
        depth(root)
        return(self.ans-1)
            