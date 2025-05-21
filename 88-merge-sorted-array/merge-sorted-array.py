class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums1[0] = min(nums1), nums1[m-1] = max(nums1)
        #nums2[0] = min(nums2), nums2[n-1] = max(nums2)
        #keep smallest, iter other
        i = m-1
        j = n-1
        k = m+n-1

        while j >= 0:
            if i >= 0 and nums2[j] < nums1[i]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j-=1
            k -= 1

            

