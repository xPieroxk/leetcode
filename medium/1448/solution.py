# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(n, max_so_far):
            if not n: return
            nonlocal ans
            if n.val >= max_so_far:
                ans += 1
                max_so_far = n.val
            dfs(n.left, max_so_far)
            dfs(n.right, max_so_far)

        dfs(root, root.val)
        return ans
