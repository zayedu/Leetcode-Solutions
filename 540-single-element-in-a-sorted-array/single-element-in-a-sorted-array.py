class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1

        while l < r:
            mid= (l+r)//2
            if mid %2:
                mid-=1

            if nums[mid+1] == nums[mid]:
                l = mid +2
            else:
                r= mid-1

        return nums[l]