class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        subsequence = [nums[0]]
        max_len = 1

        for num in nums[1:]:
            if num > subsequence[-1]:
                subsequence.append(num)
                max_len += 1

            else:
                # perform a left bisect
                l,r = 0,len(subsequence)-1

                while l < r:
                    mid = (l+r)//2

                    if subsequence[mid] < num:
                        l = mid + 1
                    else:
                        r = mid


                subsequence[l] = num

        return len(subsequence)