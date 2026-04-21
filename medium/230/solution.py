# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        i = k

        def dfs(n):
            nonlocal ans, i
            if not n or ans !=-1: return

            dfs(n.left)
            i -=1
            if i ==0:
                ans = n.val
                return
            dfs(n.right)

        dfs(root)
        return ans