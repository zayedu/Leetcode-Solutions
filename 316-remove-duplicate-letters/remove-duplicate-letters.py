class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
            
        stack = [ ]

        last_occurence = {

        }

        '''
        last_occurence:
            char -> index where it appears last
        '''
        
        for i in range(len(s)):
            last_occurence[s[i]] = i
        
        char_set = set()

        for i in range(len(s)):
            if s[i] in char_set:
                continue

            while stack and stack[-1] > s[i] and  last_occurence[stack[-1]] > i :

                char_set.remove(stack.pop())

            #we want to append when we are sure that this is the best lexocographical option
            stack.append(s[i])
            char_set.add(s[i])

        
        #s = cbacdcbc
        #last_occurence = {'a':2,'b':6,'c':7,'d':4 }
        #char_set = {'a','c','d','b'}
        #stack = ['a','c','d','b' ]

        return ''.join(stack)


        '''
        Complexity:
            Time: O(3*N)-> O(N)
            Memory: O(k)
        '''

        