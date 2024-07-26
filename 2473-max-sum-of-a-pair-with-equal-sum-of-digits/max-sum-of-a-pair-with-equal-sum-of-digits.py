class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n_as = { }
        good_arr =[-1]
        for i in nums:
            dig_sum = 0
            for j in str(i):
                dig_sum += int(j)

            if dig_sum not in n_as:
                n_as[dig_sum] = i

            else:
                good_arr.append(n_as[dig_sum]+i)
                n_as[dig_sum] = max(i,n_as[dig_sum])
        
        return max(good_arr)