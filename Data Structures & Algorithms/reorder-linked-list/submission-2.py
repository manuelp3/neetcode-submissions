# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        #find middle of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #set pointer for middle of list, create 2 separate lists
        second = slow.next
        slow.next = None

        #reverse second half
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #merge the 2 lists
        second = prev
        first = head

        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2