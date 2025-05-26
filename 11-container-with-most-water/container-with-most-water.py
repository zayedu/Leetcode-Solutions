class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0

        l,r = 0,len(nums)-1

        while l < r:
            volume = min(nums[l],nums[r]) * (r-l)
            max_volume = max(max_volume,volume)
            if nums[l] < nums[r]:
                l += 1

            else:
                r-=1

            
        return max_volume
