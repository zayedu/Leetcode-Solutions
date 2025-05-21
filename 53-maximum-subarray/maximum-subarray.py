class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[-1]
        my_sum = 0
        for i in nums:
            my_sum = max(my_sum,0)
            my_sum += i
            max_sum = max(my_sum,max_sum)

        return max_sum