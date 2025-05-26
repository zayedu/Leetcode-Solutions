class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:
        
        rows = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }

        '''
        rows should look like:
            row_num  -> set of existing nums
        '''


        cols = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }

        '''
        cols should look like:
            col_num -> set of existing nums
        '''
        squares = {
            (0,0) : set(),
            (0,1) : set(),
            (0,2) : set(),
            (1,0) : set(),
            (1,1) : set(),
            (1,2) : set(),
            (2,0) : set(),
            (2,1) : set(),
            (2,2) : set(),
        }


        for r in range(len(nums)):
            for c in range(len(nums[0])):
                element = nums[r][c]
                if element == '.':
                    continue
                if element not in rows[r]:
                    rows[r].add(element)
                else:
                    return False
                    
                if element not in cols[c]:
                    cols[c].add(element)
                else:
                    return False
                sq_idx = (c//3,r//3)

                if element in squares[sq_idx]:
                    return False
                else:
                    squares[sq_idx].add(element)

        return True

                

                
        