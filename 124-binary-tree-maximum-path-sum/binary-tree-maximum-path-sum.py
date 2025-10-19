# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            left_path = max(0,dfs(node.left))
            right_path = max(0,dfs(node.right))

            through = left_path +node.val + right_path

            max_sum = max(max_sum,through)

            return max(left_path,right_path) + node.val

        dfs(root)

        return max_sum
