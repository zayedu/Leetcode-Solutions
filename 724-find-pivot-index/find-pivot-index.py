class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums)

        my_sum = sum(nums)

        
        idx = 0
        l_val = nums[0] - nums[idx]
        r_val = my_sum - nums[idx]
        while idx < len(nums):

            r_val = my_sum - nums[idx] - l_val
            if l_val == r_val:
                return idx
            l_val += nums[idx]
            r_val += nums[idx]
            idx += 1
        return -1