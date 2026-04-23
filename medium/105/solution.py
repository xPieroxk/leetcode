# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        i = 0

        def dfs(l, r):
            if l > r:
                return None
            nonlocal i
            v = preorder[i]
            root, m = TreeNode(val=v), inorder_map[v]
            i += 1
            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)
            return root

        return dfs(0, len(preorder) - 1)
