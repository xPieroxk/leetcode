# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isValid = True

        def dfs(n):
            nonlocal isValid
            if not n or not isValid:
                return 0

            l = dfs(n.left)
            r = dfs(n.right)
            if abs(l - r) > 1:
                isValid = False
            return 1 + max(l, r)

        dfs(root)
        return isValid