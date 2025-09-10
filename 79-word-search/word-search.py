class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        '''
        seen will take (row,col) tuple of board positions
        '''
        word_possible = [False]
        def dfs(row,col, constructed_word, seen,k):

            if (row,col) in seen or row < 0 or row > len(board)-1 or col < 0 or col > len(board[0])-1 or k >= len(word) or board[row][col] != word[k]:
                return

            seen.add((row,col))
            constructed_word.append(board[row][col])
            if board[row][col] == word[k] and k == len(word)-1:
                word_possible.append(True)
                
            
            dfs(row,col+1,constructed_word, seen,k+1)
            dfs(row-1,col,constructed_word, seen,k+1)
            dfs(row+1,col,constructed_word, seen,k+1)
            dfs(row,col-1,constructed_word, seen,k+1)

            constructed_word.pop()
            seen.remove((row,col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    dfs(row,col,[],set(),0)

        return word_possible[-1]