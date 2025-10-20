class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def find_first_occurence():

            l,r = 0, len(nums)-1

            while l < r:
                mid = (l+r)//2

                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid+1

            return l if nums[l] == target else -1
        
        def find_last_occurence():

            l,r = 0, len(nums)-1

            while l < r:
                mid = (l+r+1)//2

                if nums[mid] > target:
                    r = mid-1
                else:
                    l = mid

            return l if nums[l] == target else -1
            
         
        left_point = find_first_occurence()
        right_point = find_last_occurence()


        return [left_point,right_point]

        """
        [5,7,7,8,8,10]
                 r
                 l
                    
                    m



        """