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
        
        if  topRight.x < bottomLeft.x or topRight.y < bottomLeft.y :
            return 0

        has_ships = sea.hasShips(topRight,bottomLeft)

        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y and has_ships:
            return 1

        if not has_ships:
            return 0

        mid_point_x = (bottomLeft.x + topRight.x)//2
        mid_point_y = (bottomLeft.y + topRight.y)//2

        #4 call
        q_bl = self.countShips(sea, Point(mid_point_x,mid_point_y), bottomLeft)
        q_br = self.countShips(sea, Point(topRight.x,mid_point_y),Point(mid_point_x+1,bottomLeft.y))

        q_ul = self.countShips(sea, Point(mid_point_x, topRight.y), Point(bottomLeft.x,mid_point_y+1))

        q_ur = self.countShips(sea, topRight, Point(mid_point_x + 1, mid_point_y + 1))

        return q_bl + q_br + q_ul + q_ur