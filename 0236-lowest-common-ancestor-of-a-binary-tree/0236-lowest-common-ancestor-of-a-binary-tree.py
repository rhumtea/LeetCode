# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = TreeNode(-1)
        def dfs(node):
            nonlocal res
            if not node:
                return False
            a = dfs(node.left)
            b = dfs(node.right)
            if a & b:
                res = node
            if (node == p or node == q) and (a | b):
                res = node
            return a | b | (node == p or node == q)
        dfs(root)
        return res