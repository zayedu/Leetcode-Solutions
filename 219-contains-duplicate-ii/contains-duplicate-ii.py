class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {

        }

        for index in range(len(nums)):
            if nums[index] not in seen:
                seen[nums[index]] = [index]

            else:
                for num in seen[nums[index]]:
                    if index != num and abs(num-index) <=k:
                        return True
                        
                seen[nums[index]].append(index)

        return False