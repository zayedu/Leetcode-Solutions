class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0

        last_dig = 0

        r_sum = 0
        for index in range(len(nums)):
            
            if nums[index] == 1:
                r_sum+=1
            else:
                r_sum =0
            max_ones=max(max_ones,r_sum)

        return max_ones