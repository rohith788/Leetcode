# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        d = []
        root = head
        while(root is not None):
            d.append(root.val)
            root = root.next
        return d == d[::-1]
            
            