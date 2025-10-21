class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0,len(height)-1

        left_wall,right_wall = height[0],height[r]

        water = 0 

        while l < r:
            if right_wall > left_wall:
                l += 1
                water += left_wall - height[l] if left_wall - height[l] >= 0 else 0

                left_wall = max(left_wall,height[l])

            else:
                r-=1 
                water += right_wall - height[r] if right_wall - height[r] >=0 else 0

                right_wall = max(right_wall,height[r])

        return water