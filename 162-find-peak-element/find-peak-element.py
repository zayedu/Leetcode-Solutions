class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return 0
        def binary_search(i):

            if i == 0 and nums[i] > nums[i+1]:
                return i

            if i == n-1 and nums[i] > nums[i-1]:
                return i

            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

            if i < n-1 and nums[i+1] > nums[i]:
                return binary_search(i+1)

            if i > 0 and nums[i-1] > nums[i]:
                return binary_search(i-1)

        return binary_search(int(n/2))
            