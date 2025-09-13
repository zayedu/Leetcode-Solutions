class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)

        n = len(nums)



        def dfs(index,binary):
            if index == n:
                if binary not in nums:
                    return binary

                else:
                    return False


            return dfs(index+1,binary+'1') or dfs(index+1,binary+'0')
            
        return dfs(0,'')