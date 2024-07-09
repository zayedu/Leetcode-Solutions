class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = { }
        for i in range (0,len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                my_dict[nums[i]] += 1

        result = [ ]
        
        for _ in range(k):
            max_key = max(my_dict, key = my_dict.get)  # Find the key with the maximum value
            result.append(max_key)
            my_dict[max_key] = 0  # Remove the key to find the next maximum in the next iteration
        
        return result
