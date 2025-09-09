class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_seen = {

        }
        
        '''
        let last_seen be a hashmap keeping track of when we last saw a character, this way if we see it again we know where to 
        move to so that we now no longer have a substring with a repeating character, this also acts as a seen set

        should look like:

            char -> last_seen_index
        '''
        max_nonrepeating_length = 0
        l = 0

        for r in range(len(s)):
            
            if s[r] not in last_seen:
                last_seen[s[r]] = r

            else:
                while last_seen[s[r]] >= l:
                    l += 1 

                last_seen[s[r]] = r

            max_nonrepeating_length = max(max_nonrepeating_length,r-l+1)

        return max_nonrepeating_length


