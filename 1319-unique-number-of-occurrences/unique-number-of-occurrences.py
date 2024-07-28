class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        seen = { }
        
        for i in nums:
            if i not in seen:
                seen[i] = 1

            else:
                seen[i] += 1
        seen_freq = [ ]
        for i in seen.values():
            if i in seen_freq:
                return False

            else:
                seen_freq.append(i)

        return True
