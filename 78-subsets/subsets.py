class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        out = []
        seen = set()
        
        def backtrack(arr):
            if tuple(sorted(arr)) not in seen:
                seen.add(tuple(sorted(arr)))
                out.append(list(arr))

            for num in nums:
                if num not in arr:
                    arr.append(num)
                    backtrack(arr)
                    arr.pop()
                
        backtrack([])
        return out 
