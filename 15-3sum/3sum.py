class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        result = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                    continue
            l, r = i +1, len(nums)-1
            while l < r:
                
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i],nums[l],nums[r]]) 
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    
                else:
                    r -= 1

            
        return result

