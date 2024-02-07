class Solution 
{
    public double findMedianSortedArrays(int[] nums1, int[] nums2) 
    {
        // O(log(m + n))
    
        
        // let nums1 be the shorter one
        if (nums2.length < nums1.length) return findMedianSortedArrays(nums2, nums1);
        
        // define the number of elements from nums1 that are put into the final left side
        int lo = 0;
        int hi = nums1.length;
        int N = nums1.length + nums2.length;
        
        // if N is
        // odd:  count(left) == count(right) + 1
        // even: count(left) == count(right)
        // let assume, the final state is there is p1 elements from nums1
        // and p2 elements from nums2 and there is:
        // 1: p1 + p2 == (N + 1) / 2
        // 2: nums1[p1 - 1] <= nums2[p2]
        // 3: nums2[p2 - 1] <= nums1[p1]
        // and the median is:
        // odd:  Math.max(nums1[p1 - 1], nums2[p2 - 1]) if possible
        // even: (Math.max(nums1[p1 - 1], nums2[p2 - 1]) + Math.min(nums1[p1], nums2[p2])) / 2.0 if possible
        // in both above cases, if any index is invalid then just don't use it ..
        while (lo < hi)
        {
            int p1 = (lo + hi) / 2;
            int p2 = (N + 1) / 2 - p1;
        
            if (p1 == 0 || nums1[p1 - 1] <= nums2[p2])
            {
                if (p2 == 0 || nums2[p2 - 1] <= nums1[p1]) break;
                else lo = p1 + 1;
            }
            else hi = p1 - 1;
        }
        
        int p1 = (lo + hi) / 2;
        int p2 = (N + 1) / 2 - p1;
        int m = Integer.MIN_VALUE;
        int n = Integer.MAX_VALUE;
        if (N % 2 == 1)
        {
            return Math.max(p1 - 1 >= 0 ? nums1[p1 - 1] : m, p2 - 1 >= 0 ? nums2[p2 - 1] : m);
        }
        else
        {
            return (Math.max(p1 - 1 >= 0 ? nums1[p1 - 1] : m, p2 - 1 >= 0 ? nums2[p2 - 1] : m) + 
                    Math.min(p1 < nums1.length ? nums1[p1] : n, p2 < nums2.length ? nums2[p2] : n)) / 2.0;
        }
    }
}