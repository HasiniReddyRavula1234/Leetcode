class Trie:

    def __init__(self):
        self.prefix = []

    def insert(self, word: str) -> None:
        self.prefix.append(word)

    def search(self, word: str) -> bool:
        if word in self.prefix:
            return True
        else:
            return False 

    def startsWith(self, prefix1: str) -> bool:
        for word in self.prefix:
            if word.startswith(prefix1):
                return True
        return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)