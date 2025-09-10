class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = { }

        '''
        seen is a hashmap of:
            val -> idx
        '''

        for i in range(len(nums)):
            
            if target - nums[i] in seen:
                return [seen[target-nums[i]],i]
            else:
                seen[nums[i]] = i

        return -1
        