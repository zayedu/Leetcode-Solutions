# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # divide and conquer in to quadrants
        
        hasShips = sea.hasShips(topRight,bottomLeft)

        if not hasShips:
            return 0 

        if topRight.x == bottomLeft.x or topRight.y == bottomLeft.y:
            return 1

        mid_x = (bottomLeft.x+topRight.x)//2
        mid_y = (bottomLeft.y+topRight.y)//2

        quad_bl = self.countShips(
            sea,
            Point(mid_x,mid_y),
            bottomLeft
            )

        quad_br = self.countShips(
            sea,
            Point(topRight.x,mid_y),
            Point(mid_x+1,bottomLeft.y)
            )

        quad_ul = self.countShips(
            sea,
            Point(mid_x,topRight.y),
            Point(bottomLeft.x,mid_y+1)
        )

        quad_ur = self.countShips(
            sea,
            topRight,
            Point(mid_x+1,mid_y+1)
        )

        return quad_ur + quad_ul + quad_bl + quad_br