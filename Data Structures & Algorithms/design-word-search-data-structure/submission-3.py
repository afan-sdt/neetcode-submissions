class WordDictionary:

    def __init__(self):
        self.letters = {}

    def addWord(self, word: str) -> None:
        curr = self.letters
        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr['0'] = {}

    def search(self, word: str) -> bool:
        def dfs(j, root) -> bool:
            cur = root
            for i in range(j, len(word)):
                if word[i] in cur:
                    cur = cur[word[i]]
                elif word[i] == '.':
                    for child in cur.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    return False
            if '0' in cur:
                return True
            return False
        return dfs(0, self.letters)
