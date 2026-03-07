class Solution(object):
    def containsDuplicate(self, nums):
        m = set()
        for n in nums:
            if n in m:
                return True
            m.add(n)
        return False