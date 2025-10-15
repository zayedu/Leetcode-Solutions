class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0,len(height)-1

        left_wall,right_wall = height[l],height[r]
        water  = 0
        while l < r:
            if left_wall < right_wall:
                l += 1
                water += left_wall - height[l] if left_wall - height[l] > 0 else 0

            else:
                r -= 1 
                water += right_wall - height[r] if right_wall - height[r] > 0 else 0

            left_wall = max(left_wall,height[l])
            
            right_wall = max(right_wall,height[r])

        return water


        """
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
                          ^     ^

        left_wall = 1 
        right_wall = 3

        water = 5
        """