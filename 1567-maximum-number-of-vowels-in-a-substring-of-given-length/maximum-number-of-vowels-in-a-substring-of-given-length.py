class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}

        max_vow = 0

        r_sum = 0
        l,r=0,0
        while r in range(len(s)):
            while (r-l+1) < k:
                if s[r] in vowels:
                    r_sum += 1
                r += 1


            if s[r] in vowels:
                r_sum += 1
            
            max_vow = max(max_vow, r_sum)

            if s[l] in vowels:
                r_sum -= 1
            
            l += 1
            r += 1


        return max_vow