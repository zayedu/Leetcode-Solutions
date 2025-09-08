class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        seen_freq_stack = []

        '''
        Should look like:
            [char, consecutive_count]
        '''

        for char in s:
            if seen_freq_stack and seen_freq_stack[-1][0] == char:
                seen_freq_stack.append([char,seen_freq_stack[-1][1]+1])
            else:
                seen_freq_stack.append([char,1])

            if seen_freq_stack[-1][1] == k:
                pop_iter = 0
                while pop_iter < k:
                    seen_freq_stack.pop()
                    pop_iter += 1

        return ''.join(char_info[0] for char_info in seen_freq_stack)

