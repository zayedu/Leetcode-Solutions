class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def capture(row,col):

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col]!='O':
                return

            board[row][col]= 'M'

            capture(row+1,col)
            capture(row-1,col)
            capture(row,col+1)
            capture(row,col-1)

        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col] == 'O' and (row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1):
                    capture(row,col)
                

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'M':
                    board[row][col] = 'O'
