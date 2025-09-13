class Solution:
    def compress(self, chars: List[str]) -> int:
        
        insert = 0
        i = 0

        while i < len(chars):

            group = 1

            while (group + i) < len(chars) and chars[group+i] == chars[i]:
                group += 1

            chars[insert] = chars[i]
            insert +=1
            if group > 1:
                group_str = str(group)
                chars[insert:insert+len(group_str)] = list(group_str)
                insert += len(group_str)

            i += group

        return insert