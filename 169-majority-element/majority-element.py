class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        seen = { }

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

            if seen[num] > n/2:
                return num

        return -1