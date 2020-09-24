# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        ans, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack: return ans
            node = stack.pop()
            ans.append(node.val)
            root = node.right
        
        return ans
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root: return []
    #     ans = []
    #     def helper(node: TreeNode):
    #         if node:
    #             helper(node.left)
    #             ans.append(node.val)
    #             helper(node.right)
    #     helper(root)
    #     return ans