class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l,r = 0, len(nums)-1

        while l <r:

            mid = (l+r)//2

            if nums[mid] < target:
                l = mid+1
            else:
                r= mid

        lower = l

        if nums[lower] != target:
            return [-1,-1]

        l,r = 0,len(nums)-1
        while l < r:
            mid = (l+r+1)//2

            if nums[mid]< target + 1:
                l = mid
            else:
                r= mid-1

        higher = l

        if lower<=higher:
            return [lower,higher]
        return[-1,-1]