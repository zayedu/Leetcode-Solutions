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
        
        def dfs(node, running_sum):
            if not node:
                return False
            if not node.left and not node.right:

                return running_sum + node.val== targetSum

            return dfs(node.left,running_sum+node.val) or dfs(node.right,running_sum+node.val)
                 
        return dfs(root,0)
            