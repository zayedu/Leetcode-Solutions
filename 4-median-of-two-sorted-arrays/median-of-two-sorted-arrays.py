class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n,m = len(nums1),len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2,nums1)

        total = n + m
        half = total//2

        left, right = 0, n - 1

        while True:

            midN = (left+right)//2

            midM = half - midN-2

            lower_n = nums1[midN] if midN >=0 else float('-inf')
            lower_m = nums2[midM] if midM >=0 else float('-inf')

            upper_n = nums1[midN+1] if (midN+1) < n else float('inf')
            upper_m = nums2[midM+1] if (midM+1) < m else float('inf')

            if lower_n <= upper_m and lower_m <= upper_n:

                if total %2 ==1:
                    #first element in right subarr
                    return min(upper_n,upper_m)

                else:
                    smallest_right = min(upper_n,upper_m)
                    largest_left = max(lower_n,lower_m)

                    return (smallest_right + largest_left) / 2

            elif lower_n > upper_m:
                right = midN -1

            else:
                left = midN+1




