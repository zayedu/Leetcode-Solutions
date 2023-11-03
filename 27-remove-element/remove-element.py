class Solution(object):
    def removeElement(self, nums, val):
        nums[:]=[num for num in nums if num != val]