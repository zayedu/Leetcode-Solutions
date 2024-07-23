class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [ ]
        for i in nums:
            result.append(i**2)

        return sorted(result)