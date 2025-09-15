# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def dfs(node):

            if not node:
                return [True,0]
            
            left_h = dfs(node.left)
            right_h=dfs(node.right)

            balanced = (right_h[0] and left_h[0] and abs(left_h[1]-right_h[1])<=1)
            
            return [balanced, 1+ max(left_h[1],right_h[1])]
            

        return dfs(root)[0]