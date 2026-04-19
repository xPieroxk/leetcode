# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        d = deque()
        if root:
            d.append(root)

        while d:
            level = []
            for i in range(len(d)):
                n = d.popleft()
                level.append(n.val)
                if n.left:
                    d.append(n.left)
                if n.right:
                    d.append(n.right)
            ans.append(level)

        return ans
