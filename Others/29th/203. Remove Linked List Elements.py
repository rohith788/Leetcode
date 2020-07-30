# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        curr, prev = head, temp
        while(curr):
            if curr.val == val:
                prev.next = curr.next
            else: prev = curr
            curr = curr.next
        return temp.next