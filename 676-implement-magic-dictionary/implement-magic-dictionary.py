class MagicDictionary:

    def __init__(self):
        self.word_store = defaultdict(set)
        

    def buildDict(self, dictionary: List[str]) -> None:

        for word in dictionary:
            self.word_store[len(word)].add(word)


    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.word_store:
            return False

        for word in self.word_store[len(searchWord)]:
            if self.count(word,searchWord) == 1:
                return True
            
        return False
        
    def count(self,word1,word2):
        count = 0 
        for index in range(len(word1)):
            if word1[index] != word2[index]:
                count += 1

        return count


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)