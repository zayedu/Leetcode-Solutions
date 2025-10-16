class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)

        for char in s:
            s_count[char] += 1

        for char in t:
            if char not in s_count or s_count[char] ==0:
                return False
            s_count[char] -= 1
        
        return (min(s_count.values())==0 == max(s_count.values()))