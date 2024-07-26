class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        seen = { }
        min_len = len(nums) + 1
        isValid = False
        for i in range(0,len(nums)):

            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                min_len = min(min_len,(i - seen[nums[i]] + 1))
                seen[nums[i]] = i
                isValid = True

        if isValid:
            return min_len

        return -1
