class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total//2
        l, r = 0, len(nums1)-1
        while True:
            mid = (l+r) // 2    # mid index of array of short list
            # total include actual length +2 of merged list , here we have 2 index for 2 
            #  different list bith include 0 index so for removing that we have to subtract
            # 2 from comp_mid which is long list.
            comp_mid = (half -2)- mid
        
            leftA = nums1[mid] if mid >=0 else float("-inf")
            rightA = nums1[mid+1] if (mid+1) < len(nums1) else float("inf")
            leftB = nums2[comp_mid] if comp_mid >= 0 else float("-inf")
            rightB = nums2[comp_mid+1] if (comp_mid+1) < len(nums2) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB)+ min(rightA, rightB))/2
                else:
                    return min(rightA, rightB)

            elif leftA > rightB:
                r = mid -1
            else:
                l = mid +1