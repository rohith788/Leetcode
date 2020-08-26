# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        s1, s2 = [], []
        while s1 or s2 or root1 or root2:
            while root1:
                s1.append(root1)
                root1 = root1.left
            while root2:
                s2.append(root2)
                root2 = root2.right
            if s1 and s2:
                val = s1[-1].val + s2[-1].val
            else:
                return False
            
            if val == target:
                return True
            elif val < target:
                temp = s1.pop()
                root1 = temp.right
            else:
                temp = s2.pop()
                root2 = temp.left
        return val==target