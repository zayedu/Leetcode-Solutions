class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # to maximize we want largest width and largest height
        l,r = 0 , len(height)-1
        # max width
        max_water = 0
        while l <= r:
            volume = (r - l) * min(height[l],height[r])
            max_water = max(max_water,volume)

            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1

        return max_water
