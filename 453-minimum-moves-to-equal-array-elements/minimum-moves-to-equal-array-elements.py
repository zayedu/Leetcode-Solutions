class Solution:
    def minMoves(self, nums: List[int]) -> int:
        my_moves = 0

        min_num = min(nums)

        for num in nums:
            my_moves += num- min_num 

        return my_moves