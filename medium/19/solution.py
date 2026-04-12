# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i, second = 0, head
        while i < n:
            second = second.next
            i += 1

        new_head = ListNode(0, head)
        first = new_head
        while second:
            first, second = first.next, second.next

        first.next = first.next.next
        return new_head.next
