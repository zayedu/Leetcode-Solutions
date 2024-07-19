class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        val_splits = 0

        l,r = 0,0
        l_sum = sum(nums)
        r_sum = 0
        val_splits = 0
        while l < len(nums)-1:
            r_sum += nums[r]
            l_sum -= nums[r]
            
            if r_sum >= l_sum:
                val_splits += 1
            
            r += 1
            l += 1

        return val_splits 

        



        