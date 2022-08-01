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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        var carry = 0;
        ListNode node = new ListNode();
        ListNode head = node;
        do {
            var l1Val = l1 != null ? l1.val : 0;
            var l2Val = l2 != null ? l2.val : 0;

            var sum = (l1Val + l2Val + carry);
            node.next = new ListNode(sum % 10);
            node = node.next;
            carry = sum / 10;

            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        } while (l1 != null || l2 != null || carry > 0);
        return head.next;
    }
}
