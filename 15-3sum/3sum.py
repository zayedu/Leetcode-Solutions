class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sorting the list
        result = []
        
        for i in range(len(nums)):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    
                    # Move the left pointer and skip duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Move the right pointer and skip duplicates
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
                    
        return result
