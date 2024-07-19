class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = nums[0]
        running_list = [running_sum]
        for i in range(1,len(nums)):
            running_sum += nums[i]
            running_list.append(running_sum)
        return running_list