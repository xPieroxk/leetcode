# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        enc = []

        def dfs(n):
            if not n:
                enc.append('#')
                return
            enc.append(str(n.val))
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return ','.join(enc)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        enc = data.split(',')

        def dfs():
            nonlocal i
            v = enc[i]
            i += 1
            if v == '#':
                return None
            node = TreeNode(val=int(v))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
