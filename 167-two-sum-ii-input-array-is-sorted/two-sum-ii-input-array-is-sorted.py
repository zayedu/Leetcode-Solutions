class Solution(object):
    def twoSum(self, nums, k):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0,len(nums) - 1
        res = []

        while l < r:    
            if nums[l] + nums[r] > k:
                r -= 1

            elif nums[l] + nums[r] < k:
                l += 1

            else:
                return [l+1,r+1]