from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        d = deque()
        if root:
            d.append(root)

        while d:
            size = len(d)
            for i in range(size):
                n = d.popleft()
                if i == size-1:
                    ans.append(n.val)
                if n.left:
                    d.append(n.left)
                if n.right:
                    d.append(n.right)
        return ans