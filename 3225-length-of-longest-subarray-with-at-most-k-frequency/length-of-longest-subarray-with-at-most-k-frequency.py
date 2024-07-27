class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        seen = { }
        '''
        seen should look like:
        val -> occuruences
        '''

        l = 0
        
        max_len = 0

        for r in range(len(nums)):
            if nums[r] not in seen:
                seen[nums[r]] = 1

            else:
                seen[nums[r]] += 1

            while seen[nums[r]] > k:
                ##PreConditon: We have an invalid sub array
                seen[nums[l]] -= 1
                l += 1
            #Post Condition: We have a valid sub array
            max_len = max(max_len, r - l +1)

        return max_len


        