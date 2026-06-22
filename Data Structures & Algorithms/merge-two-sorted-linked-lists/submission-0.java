/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if (list1 == null) {
            return list2;
        }
        else if (list2 == null) {
            return list1;
        }

        ListNode ptr;

        if (list1.val > list2.val) {
            ptr = list2;
            list2 = list2.next;
        }
        else {
            ptr = list1;
            list1 = list1.next;
        }

        ListNode head = ptr;

        while (list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                ptr.next = list2;
                list2 = list2.next;
            }
            else {
                ptr.next = list1;
                list1 = list1.next;
            }
            ptr = ptr.next;
        }

        if (list1 != null) {
            ptr.next = list1;
        }
        else if (list2 != null) {
            ptr.next = list2;
        }

        return head;
    }
}