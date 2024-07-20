class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        min_len = len(nums)
        
        l,r = 0, 0

        my_sum = 0
        is_valid = False
        
        while r < len(nums):

            my_sum += nums[r]
            if my_sum >= target:
                min_len = min(min_len, r - l + 1)
                is_valid = True
                break
            else:
                r += 1

        while l <= r and r < len(nums):

            if my_sum >= target:
                min_len = min(min_len, r - l + 1)
                is_valid = True
                my_sum -= nums[l]
                l += 1
            else:
                my_sum -= nums[l]
                l += 1
                r += 1
                if r < len(nums):
                    my_sum += nums[r]


        

            
        if not is_valid:
            return 0

        return min_len
