class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        def backtrack(i=0, solution=[]):
            ans.append(solution.copy())
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                solution.append(nums[j])
                backtrack(j+1, solution)
                solution.pop()
        backtrack()
        return ans