class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        odd = 0
        l,mid = 0, 0
        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1

            while odd > k:
                if nums[l] % 2:
                    odd -=1
                l += 1
                mid = l
                

            if odd == k:
                while nums[mid] % 2 == 0:
                    mid += 1
                res += (mid-l) + 1

        return res


