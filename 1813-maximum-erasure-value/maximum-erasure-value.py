class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pos = {

        }

        """
        position shoud look like:
        value -> idx
        """

        max_val = 0
        
        l = 0
        r_sum = 0
        for r in range(len(nums)):
            r_sum += nums[r]
            if nums[r] not in pos:
                pos[nums[r]] = r

            else:
                while l <= pos[nums[r]]:
                    r_sum -= nums[l]
                    l += 1
                pos[nums[r]] = r
            max_val = max(max_val, r_sum)

        return max_val