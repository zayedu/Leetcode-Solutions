class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_window = 0

        ones_freq = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                ones_freq += 1
            
            while r - l + 1 > ones_freq + k:
                if nums[l] == 1:
                    ones_freq -= 1
                l += 1 

            max_window = max(max_window, r - l + 1)

        return max_window