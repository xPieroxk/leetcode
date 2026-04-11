# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the list starting from slow (aka mid)
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge the final list
        first, second = head, prev
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


