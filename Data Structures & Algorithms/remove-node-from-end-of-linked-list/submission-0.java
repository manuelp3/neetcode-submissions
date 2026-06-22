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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int count = 0;

        for (ListNode ptr = head; ptr != null; ptr = ptr.next) {
            count++;
        }

        System.out.println(count);

        int num = count - n;

        if (num == 0) {
            head = head.next;
        }
        else {
            int cnt = 1;
            ListNode ptr;
            for (ptr = head; cnt < num; ptr = ptr.next) {
                cnt++;
            }
            ptr.next = ptr.next.next;
        }
        return head;
    }
}
