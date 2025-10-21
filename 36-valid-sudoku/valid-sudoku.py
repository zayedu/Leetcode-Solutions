class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {
            0 : set(),
            1 : set(),
            2 : set(),
            3 : set(),
            4 : set(),
            5 : set(),
            6 : set(),
            7 : set(),
            8 : set()
        }

        cols = {
            0 : set(),
            1 : set(),
            2 : set(),
            3 : set(),
            4 : set(),
            5 : set(),
            6 : set(),
            7 : set(),
            8 : set()
        }

        squares = {
            (0,0) : set(),
            (0,1) : set(),
            (0,2) : set(),
            (1,0) : set(),
            (1,1) : set(),
            (1,2) : set(),
            (2,0) : set(),
            (2,1) : set(),
            (2,2) : set()
        }

        for row in range(len(board)):
            for col in range(len(board[0])):

                value = board[row][col]
                if value == '.':
                    continue
                box = (row//3,col//3)

                if value in rows[row] or value in cols[col] or value in squares[box]:
                    return False

                rows[row].add(value)
                cols[col].add(value) 
                squares[box].add(value) 

        return True