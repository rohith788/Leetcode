# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        temp = ListNode(None)
        temp.next = head
        i = 0
        while(head):
            if( i < m-1):
                i += 1
            else: 
                j = 0
                while(j < n and head.next):
                    print(head.val)
                    head.next = head.next.next
                    j += 1
                i = 0
            head = head.next
        return temp.next