class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range (0,len(nums)):
            nums[i] *= nums[i]

        l, r = 0, len(nums)-1
        i = len(nums) - 1
        result = [ 0] *len(nums)

        while l <= r:
            if nums[l] > nums[r]:
                result[i] = nums[l]
                l += 1
                i -= 1
            else:
                result[i] = nums[r]
                r -= 1
                i -= 1

        return result


