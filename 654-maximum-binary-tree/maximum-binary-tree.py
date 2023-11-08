# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        index = 0
        curMax = -float('inf')
    
        for i in range(len(nums)):
            if nums[i] > curMax:
                curMax = nums[i]
                index = i
        
        left = self.constructMaximumBinaryTree(nums[:index])
        right = self.constructMaximumBinaryTree(nums[index + 1:])
        
        return TreeNode(curMax, left, right)  