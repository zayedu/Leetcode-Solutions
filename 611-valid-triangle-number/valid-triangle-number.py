class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()

        count = 0

        for large in range(2,len(nums)):
            left,right = 0,large-1

            while left < right:
                if nums[left] + nums[right] > nums[large]:
                    count += right - left 
                    right -= 1
                else:
                    left +=1


        return count

