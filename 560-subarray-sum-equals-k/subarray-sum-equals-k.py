class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict= {}
        cnt = 0
        my_dict[0] = 1
        my_sum = 0
        for i in nums:
            my_sum += i

            if (my_sum - k) in my_dict:
                cnt += my_dict[my_sum-k]
            if my_sum not in my_dict:
                my_dict[my_sum] = 1
            else:
                my_dict[my_sum] += 1


        return cnt
