class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left,right = 0,len(nums)-1

        while left<=right:

            mid = (right+left)//2

            if nums[mid] == target:
                return True

            if nums[left] == nums[right] == nums[mid]:
                left+=1
                right-=1
                continue 

            if nums[mid] >= nums[left]:
                #left side sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                else:
                    left = mid +1

            else:

                if nums[mid] < target <= nums[right]:
                    left = mid+1

                else:
                    right = mid - 1

        return False


