class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {

        }

        """
        freq should look like:
        val -> occurences
        """
        result = set()
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

            if freq[num] > (len(nums)/3):
                result.add(num)

        return list(result)