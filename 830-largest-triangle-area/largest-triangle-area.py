class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        max_area = 0

        for index_1 in range(len(points)):
            for index_2 in range(index_1+1,len(points)):
                for index_3 in range(index_2+1,len(points)):

                    x1,y1 = points[index_1]
                    x2,y2 = points[index_2]
                    x3,y3 = points[index_3]
                    area = 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
                    max_area = max(max_area,area)

        return max_area
