# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        cur_path = []
        cur_sum = 0
        def dfs(node, cur_path, cur_sum):
            if not node:
                return
            cur_path.append(node.val)
            cur_sum += node.val
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    res.append(list(cur_path))
            dfs(node.left, cur_path, cur_sum)
            dfs(node.right, cur_path, cur_sum)
            cur_path.pop()
        dfs(root, cur_path, cur_sum)
        return res