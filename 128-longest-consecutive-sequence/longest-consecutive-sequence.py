class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0

        for i in nums:
            if (i - 1) not in nums_set:
                length = 0
                while (i+length) in nums_set:
                    length += 1
            
                if length > longest:
                    longest = length

        return longest


