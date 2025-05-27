from collections import deque


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = deque()
        i = len(a)-1
        j=len(b)-1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i>=0 else 0
            digit_b = int(b[j]) if j>=0 else 0
            sum = digit_a + digit_b + carry
            ans.appendleft(str(sum%2))
            carry = sum // 2
            i-=1
            j-=1
        return ''.join(ans)
