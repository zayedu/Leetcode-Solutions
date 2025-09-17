class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0,len(height)-1
        max_l, max_r = height[l],height[r]
        water = 0
        
        while l<r:

            if max_r < max_l:

                water += 0 if max_r - height[r] < 0 else max_r - height[r]
                r-= 1
                max_r = max(height[r],max_r)

            else:
                water += 0 if max_l - height[l] < 0 else max_l - height[l]
                l+= 1
                max_l = max(height[l],max_l)
        
        return water






