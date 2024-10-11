class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        
        prev_positions = {(0,0)}

        """
        prev positions contains all past positions as tuples.
        ex. [(0,0),(0,1)...]
        """
        position = [0,0]
        for move in path:
            if move == 'N':
                position[1] += 1
            elif move == 'S':
                position[1] -= 1
            elif move == 'E':
                position[0] += 1
            elif move == 'W':
                position[0] -= 1


            
            if tuple(position) in prev_positions:
                return True
            prev_positions.add(tuple(position))

        return False
            
            
            
