class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows ={
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
        }

        cols ={
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
        }

        boxes = {
            (0,0): set(),
            (0,1): set(),
            (0,2): set(),
            (1,0): set(),
            (1,1): set(),
            (1,2): set(),
            (2,0): set(),
            (2,1): set(),
            (2,2): set()
        }

        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val == '.':
                    continue
                box = (row//3,col//3)

                if val in rows[row] or val in cols[col] or val in boxes[box]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                boxes[box].add(val)

        return True
