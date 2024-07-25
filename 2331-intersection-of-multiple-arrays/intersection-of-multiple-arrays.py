class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        numbers = {}
        result = []
        for _nums in nums:
            for i in _nums:
                if i not in numbers:
                    numbers[i] = 1
                else:
                    numbers[i] += 1
                if numbers[i] == len(nums):
                    result.append(i)
        
        return sorted(result)