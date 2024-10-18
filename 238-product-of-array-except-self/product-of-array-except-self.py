class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

        """
        Complexity:
        Time = O(2n) -> O(n)
        Space = O(n)
        """