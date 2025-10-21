class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern_map = {} #pattern[index] -> s[index]

        arr_s = s.split(' ')

        if len(arr_s) != len(pattern):
            return False

        for index in range(len(pattern)):
            if pattern[index] not in pattern_map:
                if arr_s[index] in pattern_map.values():
                    return False

                pattern_map[pattern[index]] = arr_s[index]

            else:
                if pattern_map[pattern[index]] != arr_s[index]:
                    return False
                

        return True

        """
        abba 

        dog cat cat dog

        """