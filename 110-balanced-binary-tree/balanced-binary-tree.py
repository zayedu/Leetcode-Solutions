# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):

            if not node:
                return [True,0]
                
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            if left_h[0] and right_h[0] and abs(left_h[1]-right_h[1]) <= 1:

                return [True,1+max(left_h[1],right_h[1])]

            return [False,1+max(left_h[1],right_h[1])]

        return dfs(root)[0]


