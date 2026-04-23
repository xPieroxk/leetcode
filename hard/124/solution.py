# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(n):
            if not n: return 0
            nonlocal ans
            l = dfs(n.left)
            l = l if l >= 0 else 0
            r = dfs(n.right)
            r = r if r >= 0 else 0
            ans = max(ans, n.val + l + r)
            return n.val + max(l, r)

        dfs(root)
        return ans
