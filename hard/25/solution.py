# initial solution
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(h):
            prev = None
            head = h
            t = 0
            while t < k:
                tmp = h.next
                h.next = prev
                prev = h
                h = tmp
                t += 1
            return prev, head

        curr, curr_head = head, head
        last_tail = None
        i = 0
        while curr:
            if i == k:
                r_head, r_tail = reverse(curr_head)
                if last_tail:
                    last_tail.next = r_head
                else:
                    head = r_head
                r_tail.next = curr
                curr_head = curr
                last_tail = r_tail
                i = 0
            curr = curr.next
            i += 1

        if i == k:
            r_head, r_tail = reverse(curr_head)
            if last_tail:
                last_tail.next = r_head
            else:
                head = r_head

        return head
# refined solution with dummy pointer

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(next=head)
        group_prev_tail = dummy

        while True:
            kth = getKth(group_prev_tail, k)
            if not kth:
                break

            stop = kth.next
            prev, curr = kth.next, group_prev_tail.next
            while curr != stop:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = group_prev_tail.next
            group_prev_tail.next = kth
            group_prev_tail = tmp

        return dummy.next

