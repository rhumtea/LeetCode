# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visit = set()
        cnt = defaultdict(int)
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return "#"
            a = dfs(node.left)
            b = dfs(node.right)
            t = f"{node.val}, {a}, {b}"
            if cnt[t] == 1:
                res.append(node)
            cnt[t] += 1
            return t
        dfs(root)
        return res