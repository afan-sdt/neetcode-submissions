class TrieNode:
    def __init__(self, char):
        self.nextLetter = {}
        self.character = char
class PrefixTree:

    def __init__(self):
        self.head = TrieNode('#') 

    def insert(self, word: str) -> None:
        curr = self.head
        for x in word:
            if x not in curr.nextLetter:
                curr.nextLetter[x] = TrieNode('x')
            curr = curr.nextLetter[x]
        curr.nextLetter['#'] = TrieNode('#')

    def search(self, word: str) -> bool:
        curr = self.head
        for x in word:
            if x not in curr.nextLetter:
                return False
            else:
                curr = curr.nextLetter[x]
        if '#' in curr.nextLetter:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for x in prefix:
            if x not in curr.nextLetter:
                return False
            else:
                curr = curr.nextLetter[x]
        return True
        