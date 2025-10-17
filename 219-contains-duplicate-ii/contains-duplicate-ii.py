class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {

        }

        for index in range(len(nums)):

            if nums[index] in seen:
                if abs(index - seen[nums[index]]) <=k:
                    return True
                
            seen[nums[index]] = index

        return False
