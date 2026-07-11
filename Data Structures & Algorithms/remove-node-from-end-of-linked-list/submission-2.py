# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        end = head
        for i in range(n):
            end = end.next
        
        if not end:
            return head.next

        while end:
            dummy = dummy.next
            end = end.next
        
        dummy.next = dummy.next.next
        return head