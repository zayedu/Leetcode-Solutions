class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        init_sv = 1

        
        sv = 1
        i = 0
        while i < len(nums):
            sv += nums[i]
            if sv < 1:
                i = 0
                init_sv += 1
                sv = init_sv
            else:
                i += 1

        return init_sv



