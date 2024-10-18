class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        l = 0
        l_val = 0

        r_val = sum(nums)

        valid_splits = 0

        for r in range(len(nums)-1):
            l_val += nums[l]
            r_val -= nums[l]

            if l_val >= r_val:
                valid_splits += 1
            l += 1

        return valid_splits
