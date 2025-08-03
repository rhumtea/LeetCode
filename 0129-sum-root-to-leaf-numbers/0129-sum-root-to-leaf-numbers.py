# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, cur_path, cur_str):
            nonlocal res
            if not node:
                return
            cur_path.append(node.val)
            cur_str += str(node.val)
            print(cur_path)
            print(cur_str)
            if not node.left and not node.right:
                res += int(cur_str)
            dfs(node.left, cur_path, cur_str)
            dfs(node.right, cur_path, cur_str)
            cur_path.pop()
        dfs(root, [], "")
        return res 