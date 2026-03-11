class Node:
    def __init__(self, prev=None, next=None):
        self.prev = prev
        self.next = next


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = {}

        for n in nums:
            curr = Node()
            if n - 1 in sequences:
                sequences[n - 1].next = curr
                curr.prev = sequences[n - 1]
            if n + 1 in sequences:
                sequences[n + 1].prev = curr
                curr.next = sequences[n + 1]
            sequences[n] = curr

        max_len = 0

        for k in sequences:
            curr = sequences[k]
            if not curr.prev:
                curr_len = 0
                while curr:
                    curr = curr.next
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len
