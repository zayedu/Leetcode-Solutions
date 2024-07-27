

class Solution:
    def frequencySort(self, s: str) -> str:
        seen = { }

        '''
        seen should look like:
        char -> occurences
        '''

        for char in s:
            if char not in seen:
                seen[char] = 1

            else:
                seen[char] += 1

        '''
        seen:
        t -> 1
        r -> 1
        e -> 2
        
        seen.items()
        [(t,1),(r,1),(e,2)]
        '''             

        sorted_occurences = sorted(seen.items(),reverse = True, key = lambda x:x[1])

        '''
        sorted_occurences:
        [(e,2),(t,1),(r,1)]
        '''
        result = [ ]

        '''
        result:
        []
        [e,t,r]
        '''

        for key ,value in sorted_occurences:
            for addr in range(value):
                result.append(key)
        
        return ''.join(result)
