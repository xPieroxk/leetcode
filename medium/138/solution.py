"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        original = head
        while original:
            tmp = original.next
            original.next = Node(original.val, tmp)
            original = tmp

        original = head
        while original:
            if original.random:
                original.next.random = original.random.next
            original = original.next.next

        original, new_head = head, head.next
        while original:
            copy = original.next
            original.next = copy.next
            if copy.next:
                copy.next = copy.next.next

            original = original.next

        return new_head