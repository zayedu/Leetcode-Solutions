class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        r_sum = nums[0]
        max_ones = r_sum

        for index in range(1,len(nums)):
            if nums[index] == 0:
                r_sum = 0 

            if nums[index] == 1:
                r_sum += 1

            max_ones = max(r_sum,max_ones)


        return max_ones