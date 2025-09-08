class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        seen_freq_stack = []

        '''
        Should look like:
            [char, consecutive_count]
        '''

        for char in s:
            if seen_freq_stack and seen_freq_stack[-1][0] == char:
                seen_freq_stack[-1][1] += 1
            else:
                seen_freq_stack.append([char,1])

            if seen_freq_stack[-1][1] == k:
                seen_freq_stack.pop()
        answer = ''
        for char_info in seen_freq_stack:
            answer += char_info[1]*char_info[0]

        return answer

