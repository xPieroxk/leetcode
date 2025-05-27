# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        current = head
        while current.next:
            # skip duplicates
            if current.val == current.next.val:
                current.next = current.next.next
            # update next if different
            else:
                current = current.next

        return head
