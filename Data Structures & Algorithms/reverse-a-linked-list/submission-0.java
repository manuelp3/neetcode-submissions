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
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        
        Stack<ListNode> stack = new Stack<>();

        for (ListNode ptr = head; ptr != null; ptr = ptr.next) {
            stack.push(ptr);
        }

        ListNode newHead = stack.pop();
        ListNode ptr = newHead;

        while (!stack.isEmpty()) {
            ptr.next = stack.pop();
            ptr = ptr.next;
        }
        ptr.next = null;

        return newHead;
    }
}
