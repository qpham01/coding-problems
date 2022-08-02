from operator import le
from tree_node import TreeNode

class WordTrie:
    def __init__(self):
        self.root = TreeNode("")
        self.words = set()
        
    def addWord(self, word:str, parent:TreeNode = None, index:int = 0):
        if index >= len(word): return
        if parent is None: 
            parent = self.root
            self.words.add(word)
        letter = word[index]
        child =  parent.children[letter] if letter in parent.children.keys() else parent.addChild(letter)
        self.addWord(word, child, index + 1)

    def getWords(self, snippet:str):
        words = set()
        current = ""
        self.dfs(self.root, current, words, snippet, 0)
        word_list = list(words)
        word_list.sort()
        return word_list
        
    def dfs(self, node:TreeNode, current:str, words:set, snippet:str, index:int):
        current = current + node.data
        length = len(snippet)
        if index >= length and current in self.words:
            words.add(current)
        if index < length:
            letter = snippet[index]
            next = node.children.get(letter)
            if not next: return
            self.dfs(next, current, words, snippet, index + 1)
        for key in node.children.keys():
            self.dfs(node.children[key], current, words, snippet, index)
                