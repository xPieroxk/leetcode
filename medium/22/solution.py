class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def bt(curr, opened, closed):
            if closed > opened or opened > n:
                return
            if opened == closed == n:
                ans.append("".join(curr))
                return

            curr.append("(")
            bt(curr, opened + 1, closed)

            curr.pop()
            curr.append(")")
            bt(curr, opened, closed + 1)

            curr.pop()

        bt([], 0, 0)
        return ans