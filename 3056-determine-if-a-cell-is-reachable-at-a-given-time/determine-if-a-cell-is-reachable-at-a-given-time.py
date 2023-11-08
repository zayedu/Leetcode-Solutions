class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_distance = abs(sx - fx)
        y_distance = abs(sy - fy)

        if x_distance ==0 and y_distance==0:
            return t!=1

        return x_distance <=t and y_distance<=t