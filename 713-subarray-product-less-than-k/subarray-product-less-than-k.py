class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0

        result = 0
        l,r = 0,0
        product = 1

        while r < len(nums):
            
            product *= nums[r]

            while l<=r and product >= k:
                product /= nums[l]
                l += 1
            
            result += (r-l+1)



            r += 1
        return result