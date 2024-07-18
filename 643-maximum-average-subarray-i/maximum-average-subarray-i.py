class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        
        l = 0
        r = k-1
        max_sum = 0.0
        for i in range (0,k):
            max_sum += nums[i]

        sum_iter = max_sum
        print(sum_iter)
        sum_iter -= nums[l]
        print(sum_iter)
        
        l += 1
        r += 1
        while r < len(nums):
            print(nums[r])
            sum_iter += nums[r]
            print(sum_iter)

            max_sum = max(max_sum,sum_iter)
            sum_iter -= nums[l]
            l += 1
            r += 1


        return (max_sum/float(k))