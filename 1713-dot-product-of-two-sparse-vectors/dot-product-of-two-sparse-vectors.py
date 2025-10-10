class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.vector = nums
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotted_vec = 0
        for index in range(len(self.vector)):
            dotted_vec += self.vector[index]*vec.vector[index]

        return dotted_vec

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)