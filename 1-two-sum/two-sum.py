class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range (0,len(nums)):
            look = target - nums[i]
            if look in my_dict:
                return [my_dict[look],i]
            my_dict[nums[i]] = i

