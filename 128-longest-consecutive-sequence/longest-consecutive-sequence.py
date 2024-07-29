class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        length,longest = 0,0

        for i in nums_set:
            if (i - 1) not in nums_set:
                length = 0
                while (i+length) in nums_set:
                    length += 1
            
                longest = max(length,longest)

        return longest
            
        
                
        