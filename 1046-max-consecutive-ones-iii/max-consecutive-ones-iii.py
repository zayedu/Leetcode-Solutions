class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        f_cnt = 0
        max_count = 0

        while r < len(nums):
            if nums[r] == 0:
                f_cnt += 1

            while f_cnt > k:
                if nums[l] == 0:
                    f_cnt -= 1
                l += 1

            max_count = max(max_count, r - l + 1)
            r += 1

        return max_count