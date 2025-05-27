class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        m -= 1
        n -= 1
        nextPosition = n + m + 1
        while n >= 0:

            if m >= 0 and nums1[m] > nums2[n]:
                nums1[nextPosition] = nums1[m]
                m -= 1
            else:
                nums1[nextPosition] = nums2[n]
                n -= 1
            nextPosition -= 1
