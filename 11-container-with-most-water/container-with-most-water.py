class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height)-1
        max_volume = 0
        
        while l < r:
            volume = min(height[l],height[r])* (r-l)
            max_volume = max(max_volume,volume)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_volume
