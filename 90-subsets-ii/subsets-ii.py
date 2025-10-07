class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets = []
        subset = []
        def backtrack(index=0):
            if index == len(nums):
                subsets.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index+1)
            subset.pop()
            while (index +1) < len(nums) and nums[index] == nums[index+1]:
                index+=1

            
            backtrack(index+1)


        backtrack()

        return subsets