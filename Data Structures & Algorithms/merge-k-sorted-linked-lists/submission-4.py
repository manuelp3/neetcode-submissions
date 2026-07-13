# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head = lists[0]
        for i in range(1, len(lists)):
            curr = lists[i]
            ptr = head
            prev = None
            if curr.val < head.val:
                temp = curr.next
                curr.next = ptr
                head = curr
                ptr = curr
                curr = temp
            while curr and ptr:
                if (curr.val < ptr.val):
                    temp = curr.next
                    prev.next = curr
                    curr.next = ptr
                    prev = curr
                    curr = temp
                else:
                    prev = ptr
                    ptr = ptr.next
            if curr:
                prev.next = curr
        return head