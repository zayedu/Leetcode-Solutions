class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            beginIndex1, beginIndex2 = 0, 0
            while True:
                if beginIndex1 == m:
                    return nums2[beginIndex2 + k - 1]
                if beginIndex2 == n:
                    return nums1[beginIndex1 + k - 1]
                if k == 1:
                    return min(nums1[beginIndex1], nums2[beginIndex2]) 

                pivotIndex1 = min(beginIndex1 + k//2 - 1, m - 1)
                pivotIndex2 = min(beginIndex2 + k//2 - 1, n - 1)
                pivot1 = nums1[pivotIndex1]
                pivot2 = nums2[pivotIndex2]

                if pivot1 <= pivot2:
                    k -= pivotIndex1 - beginIndex1 + 1
                    beginIndex1 = pivotIndex1 + 1
                else:
                    k -= pivotIndex2 - beginIndex2 + 1
                    beginIndex2 = pivotIndex2 + 1             

        m, n = len(nums1), len(nums2)
        length = m + n
        if length % 2 == 1:
            return getKthElement(length//2 + 1)
        else:
            return (getKthElement(length//2) + getKthElement(length//2 + 1)) / 2