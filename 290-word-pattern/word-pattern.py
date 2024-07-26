class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat = { }

        '''
        pat should look like pattern[char] -> s[word]
        '''

        arr = s.split()
        if len(arr) != len(pattern):
            return False

        for i in range(len(arr)):
            if pattern[i] not in pat and arr[i] not in pat.values():
                pat[pattern[i]] = arr[i]

            elif arr[i] in pat.values():
                _key = ''
                for k,v in pat.items():
                    if v == arr[i]:
                        _key = k

                if _key != pattern[i]:
                    return False
            else:
                if pat[pattern[i]] != arr[i]:
                    return False

        return True
        