class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        if k > n:
            return [-1] * n
        
        if k == 0:
            return nums
        
        result = [-1] * n
        
        mid = k
        l = 0
        r = mid + k
        
        if r >= n:
            return result
        
        avg = sum(nums[l:r+1])
        
        while r < n:
            result[mid] = avg // (2 * k + 1)
            mid += 1
            avg -= nums[l]
            l += 1
            r += 1
            if r < n:
                avg += nums[r]
        
        return result