class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # store indices, not heights
        water = 0

        for i in range(len(height)):
            # While current bar is higher than the bar at stack top, we can trap water
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break  # no left wall
                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[left], height[i]) - height[bottom]
                if bounded_height > 0:
                    water += width * bounded_height
            stack.append(i)

        return water
