class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [False] * (len(nums)+1)

        for i in nums:
            arr[i] = True

        for i in range(len(arr)):
            if arr[i] == False:
                return i