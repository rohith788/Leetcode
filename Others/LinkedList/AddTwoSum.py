# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = node = ListNode(0)
        while l1 or l2 or carry:
            temp1 = temp2 = 0
            if l1:
                temp1 = l1.val
                l1 = l1.next
            if l2:
                temp2 = l2.val
                l2 = l2.next
            sum = temp1 + temp2 + carry
            carry = sum // 10
            
            node.next = ListNode(sum % 10)
            node = node.next
        return head.next
            