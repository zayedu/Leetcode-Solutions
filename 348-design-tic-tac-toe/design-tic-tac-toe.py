class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.positive_diagonal = 0
        self.negative_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1
        self.rows[row] += val
        self.cols[col] += val

        if row == col:
            self.negative_diagonal += val
        if row == self.n - col -1:
            self.positive_diagonal += val
        
        if (abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.negative_diagonal)==self.n or abs(self.positive_diagonal)==self.n):
            return player
            
        return 0

        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)