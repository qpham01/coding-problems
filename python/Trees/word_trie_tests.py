from word_trie import WordTrie

trie = WordTrie()
trie.addWord("a")
trie.addWord("an")
trie.addWord("and")
trie.addWord("annoy")
trie.addWord("annoyance")
trie.addWord("annoying")
trie.addWord("anorexia")

aWords = trie.getWords("a")
print("a", aWords)
assert len(aWords) == 7

anWords = trie.getWords("an")
print("an", anWords)
assert len(anWords) == 6
assert "a" not in anWords

andWords = trie.getWords("and")
print("and", andWords)
assert len(andWords) == 1
assert "and" in andWords

annWords = trie.getWords("ann")
print("ann", annWords)
assert len(annWords) == 3
assert "a" not in annWords
assert "an" not in annWords
assert "ann" not in annWords

annoyWords = trie.getWords("annoy")
print("annoy", annoyWords)
assert len(annoyWords) == 3
assert "annoy" in annoyWords


