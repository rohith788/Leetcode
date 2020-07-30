# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = {}
        while(head):
            if head in d: return True
            else: d[head] = " "
            head = head.next
        return False