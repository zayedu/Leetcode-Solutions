class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        direct_match = set(wordlist)
        case_match = {}
        vowel_match = {}

        for word in wordlist:

            if word.lower() not in case_match:
                case_match[word.lower()] = word
            if self.unvowel(word) not in vowel_match:
                vowel_match[self.unvowel(word)] = word

        spell_checked = []
        for query in queries:
            if query in direct_match:
                spell_checked.append(query)

            elif query.lower() in case_match:
                spell_checked.append(case_match[query.lower()])

            elif self.unvowel(query) in vowel_match:
                spell_checked.append(vowel_match[self.unvowel(query)])
            
            else:
                spell_checked.append("")

        return spell_checked


    def unvowel(self,word):
        vowels = {'a','e','i','o','u'}
        word = word.lower()
        out = []
        for char in word:
            if char in vowels:
                out.append('*')
            else:
                out.append(char)
        return  ''.join(out)



