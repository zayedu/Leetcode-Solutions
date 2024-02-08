class Solution(object):
    def binarySearch(self, nums: List[int], start: int, end: int, num: int) -> int:
        if(start == end):
            return start
        mid = int((start + end + 1)/2)
        if(nums[mid] < num):
            return self.binarySearch(nums, mid, end, num)
        elif(nums[mid] > num) :
            return self.binarySearch(nums, start, mid-1, num)
        return mid

    #Tries to find the element in the nums1 array which is the nearest to required position {req} in the combined sorted list.
    def findMiddleMostElement(self, nums1: List[int], nums2: List[int], req: int) :
        start1 = 0
        end1 = len(nums1) - 1
        best_pos = sys.maxsize #position in the combined sorted list
        best_index = -1        #index in the nums1 array
        
        while(start1 <= end1) :
            mid1 = int((start1 + end1 + 1)/2)
            tmp2 = self.binarySearch(nums2, 0, len(nums2)-1, nums1[mid1])
            pos = mid1+tmp2+1 if(nums2[tmp2] < nums1[mid1]) else mid1+tmp2
            
            if(abs(req - pos) < best_pos) :
                best_pos = pos
                best_index = mid1
                
            if(req == pos) : 
                return (mid1, pos)
            elif(req < pos) :
                end1 = mid1 - 1
            else :
                start1 = mid1 + 1
        
        return (best_index, best_pos)
            
            

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #EdgeCases
        if(len(nums1) == 0 or len(nums2) == 0) :
            if(len(nums1) == 0) :
                nums1 = nums2
            if(len(nums1)%2 == 0) :
                return (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2 -1)])/2
            else :
                return nums1[int(len(nums1)/2)]
        
        #StartsHere
        (ind1, pos1) = self.findMiddleMostElement(nums1, nums2, int((len(nums1) + len(nums2))/2))
        (ind2, pos2) = self.findMiddleMostElement(nums2, nums1, int((len(nums1) + len(nums2))/2))
        
        total = len(nums1) + len(nums2)
        req1 = int((len(nums1) + len(nums2))/2)      
        
        if(total %2 != 0) :
            if(req1 == pos1) : 
                return nums1[ind1]
            else : 
                return nums2[ind2]
        
        
        req2 = int((len(nums1) + len(nums2))/2) - 1 
        
        (i1,p1) =  self.findMiddleMostElement(nums1, nums2, int((len(nums1) + len(nums2))/2) -1)
        (i2,p2) =  self.findMiddleMostElement(nums2, nums1, int((len(nums1) + len(nums2))/2) -1)    
        
        sums = (nums1[ind1] if pos1==req1 else nums2[ind2]) + (nums1[i1] if p1 == req2 else nums2[i2])
        
        return sums/2