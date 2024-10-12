class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        freq = {

        }

        """
        freq should look like:
        value -> freq
        """

        l = 0
        max_sub = 0
        for r in range (len(nums)):
            if nums[r] not in freq:
                freq[nums[r]] = 1
            else:
                freq[nums[r]] += 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1

            max_sub = max(max_sub, r-l+1)

        return max_sub