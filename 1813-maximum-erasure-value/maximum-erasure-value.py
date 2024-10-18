class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        seen = {

        }
         
        """
        Seen hashmap should like:
        num -> idx
        """

        max_sum = 0
        r_sum = 0

        l = 0
        for r in range(len(nums)):
            r_sum += nums[r]
            if nums[r] not in seen:
                seen[nums[r]] = r

            else:
                while l <= seen[nums[r]]:
                    r_sum -= nums[l]
                    l += 1
                seen[nums[r]] = r
            
            max_sum = max(max_sum,r_sum)

        return max_sum



        """
        Complexity:
        Time = O(n)
        Space = O(n)
        where n is the length of nums
        """
        