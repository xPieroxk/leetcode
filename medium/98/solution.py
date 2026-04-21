# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(n, left_bound, right_bound):
            if not n: return True
            if n.val >= right_bound or n.val <= left_bound:
                return False

            is_right_valid = dfs(n.right, n.val, right_bound)
            is_left_valid = dfs(n.left, left_bound, n.val)

            return is_left_valid and is_right_valid

        return dfs(root, float('-inf'), float('inf'))