# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(q, p):
            if not q and not p:
                return True
            if not q or not p or q.val != p.val:
                return False
            return sameTree(q.left, p.left) and sameTree(q.right, p.right)

        stack = []
        if root:
            stack.append(root)

        while stack:
            n = stack.pop()
            if sameTree(n, subRoot):
                return True
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

        return False