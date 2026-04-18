class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            curr = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1:
                curr.next = l1
            if l2:
                curr.next = l2

            return dummy.next

        while len(lists) > 1:
            tmp = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                tmp.append(merge(list1, list2))

            lists = tmp

        return lists[0] if len(lists) == 1 else None
