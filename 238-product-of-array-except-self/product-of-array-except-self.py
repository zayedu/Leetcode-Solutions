class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = 1 
        result = [1,]
        for i in range(0,len(nums)-1):
            pre = pre * nums[i]
            result.append(pre)

        post = 1 
        for i in range (len(nums)-1,0,-1):
            post = post * nums[i]
            result[i-1] = result[i-1]*post

        return result
        
            

