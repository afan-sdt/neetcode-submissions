class PrefixTree:

    def __init__(self):
        self.letters = {}

    def insert(self, word: str) -> None:
        curr = self.letters
        for i in word:
            if i in curr:
                curr = curr[i]
            else:
                curr[i] = {}
                curr = curr[i]
        curr['0'] = 0
        

    def search(self, word: str) -> bool:
        curr = self.letters
        for i in word:
            if i in curr:
                curr = curr[i]
            else:
                return False
        if '0' in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.letters
        for i in prefix:
            if i in curr:
                curr = curr[i]
            else:
                return False
        return True