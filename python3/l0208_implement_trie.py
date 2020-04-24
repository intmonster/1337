class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = { 'root': {} }
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self._trie['root']
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[''] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._trie['root']
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._trie['root']
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)