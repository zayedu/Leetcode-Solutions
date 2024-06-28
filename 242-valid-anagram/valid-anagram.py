class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = dict()
        for i in range (0,len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = 1 
            else:
                my_dict[s[i]] += 1

        for i in range (0,len(t)):
            if t[i] not in my_dict:
                return False

            my_dict[t[i]] -= 1
        
        print(my_dict)

        for i in my_dict.values():
            if i != 0:
                return False

        return True 
