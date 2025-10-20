class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        """
        [10,9,2,5,3,7,101,18] -> [2,3,7,101] | [2,5,7,101]
                    ^
        [0,1,0,3,2,3] -> [0,1,2,3]
                   ^

        subsequence  = []
        num > end
        """

        subsequence = [nums[0]]

        for num in nums:

            if num > subsequence[-1]:
                subsequence.append(num)
            else:
                # replacement with a left bisect

                l,r = 0, len(subsequence)-1

                while l < r:
                    mid = (l+r)//2

                    if subsequence[mid] < num:
                        l = mid+1
                    else:
                        r = mid

                subsequence[l] = num

        return len(subsequence)