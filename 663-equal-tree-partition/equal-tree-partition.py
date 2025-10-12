# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sums = []

        def dfs(node):
            if not node:
                return 0

            subtree_sum = node.val + dfs(node.left) + dfs(node.right)

            sums.append(subtree_sum)

            return subtree_sum

        total = dfs(root)
        sums.pop()

        if total%2 != 0:
            return False
            
        return total//2 in sums 