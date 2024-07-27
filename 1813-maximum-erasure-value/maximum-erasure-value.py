class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        max_score, ctr = 0,0

        l = 0 
        seen = { }
        '''
        seen should look like:
        val -> last idx
        '''

        for r in range(len(nums)):
            if nums[r] not in seen:
                seen[nums[r]] = r
                ctr += nums[r]

            else:
                while l <= seen[nums[r]]:
                    ctr -= nums[l]
                    l += 1
                seen[nums[r]] = r
                ctr += nums[r]
                

            max_score = max(ctr,max_score)
        return max_score