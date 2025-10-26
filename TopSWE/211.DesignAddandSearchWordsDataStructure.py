# 211. Design Add and Search Words Data Structure
# Medium
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
# Explnation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


# KINDA TRICKY the main thing is the search function where we have to do a dfs when we encounter a '.' char
# Doing a recursive dfs search function to handle the '.' char case so make sure to understand it carefully
class WordDictionary:

    def __init__(self):
        self.children={}
        self.End=False

    def addWord(self, word: str) -> None:
        node =self
        for c in word:
            if c not in node.children:
                node.children[c]=WordDictionary()
            node=node.children[c]
        node.End=True

    def search(self, word: str) -> bool:
        def dfs(j,node):
            for i in range(j,len(word)):
                c=word[i]
                if c==".":
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node=node.children[c]
            return node.End
        return dfs(0,self)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)