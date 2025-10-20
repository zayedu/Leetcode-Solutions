class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = max(heights)

        stack = [] #[height,index]

        for index in range(len(heights)):
            start = index
            while stack and stack[-1][0] > heights[index]:
                h,start= stack.pop()
                area  = h * (index-start)
                max_area = max(max_area,area)

            stack.append([heights[index],start])

        for h,index in stack:
            max_area = max(max_area, h*(len(heights)-index))


        return max_area

        """
        max_area = 10

        [2,1,5,6,2,3]
index              ^
start:             ^
h = 5
         stack = [
            [1,0],
            [2,2],
            [3,5] <-
         ] //top of our sack


        """