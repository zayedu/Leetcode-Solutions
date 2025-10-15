class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets= []

        def backtrack(index,subset):
            if index ==len(nums):
                subsets.append(subset)
                return

            subset.append(nums[index])
            backtrack(index+1,subset.copy())
            subset.pop()
            while index +1 < len(nums) and nums[index+1] == nums[index]:
                index+=1

            
            backtrack(index+1,subset.copy())

        backtrack(0,[])

        return subsets

            

            