# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        path_sums = set()

        def dfs(node,path_sum):
            
            if not (node.left or node.right):
                path_sums.add(path_sum)
                return

            if node.left:
                dfs(node.left,path_sum+node.left.val)

            if node.right:
                dfs(node.right,path_sum+node.right.val)

        dfs(root,root.val)
        return targetSum in path_sums

            
