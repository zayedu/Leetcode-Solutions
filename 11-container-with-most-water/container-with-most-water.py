class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_wtr = 0
        l = 0
        r = len(height) - 1 
        while l <= r:
            wtr = ((r-l)*min(height[r],height[l]))
            max_wtr = max(max_wtr,wtr)

            if height[r] > height[l]:
                l += 1

            else:
                r -= 1
        return max_wtr
        