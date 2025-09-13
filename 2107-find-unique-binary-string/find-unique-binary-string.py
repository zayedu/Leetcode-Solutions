class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ['0']*len(nums)

        for index in range(len(nums)):
            ans[index] = '1' if str(nums[index])[index] == '0' else '0'

        return "".join(ans)