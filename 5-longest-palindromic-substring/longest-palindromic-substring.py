class Solution:

    def isPal(self,s,left,right):

        while left >= 0 and right < len(s) and s[left] == s[right] :
            left-=1
            right +=1

        return left+1,right-1, right - left+1-2

    def longestPalindrome(self, s: str) -> str:
        left,right = 0,0
        max_len = 1

        for mid in range(len(s)):

            l,r,length = self.isPal(s,mid,mid)

            if length > max_len:
                max_len = length
                left,right = l,r

            l,r,length = self.isPal(s,mid,mid+1)

            if length > max_len:
                max_len = length
                left,right = l,r
        
        return s[left:right+1]