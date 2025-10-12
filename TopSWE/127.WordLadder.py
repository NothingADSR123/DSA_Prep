# 127. Word Ladder
# HARD
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWor
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

from typing import List,list,defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bank=set(wordList)
        # visited=set([beginWord])              #DID KHUDSE HEllo
        # if endWord not in bank: return 0
        # q=deque([(beginWord,1)])
        # chars="qwertyuiopasdfghjklzxcvbnm"
        # while q:
        #     g,steps=q.popleft()
        #     if g == endWord: return steps
        #     for i in range(len(g)):
        #         for c in chars:
        #             if c == g[i]:
        #                 continue
        #             new=g[:i]+c+g[i+1:]
        #             if new in bank and new not in visited:
        #                 visited.add(new)
        #                 q.append((new,steps+1))
        # return 0

        # OPTIMAL APPROACH PATTERN 
        if endWord not in wordList: return 0
        nei=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        visited=set([beginWord])
        q=deque([beginWord])
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord: return res
                for i in range(len(word)):
                    pattern=word[:i]+"*" + word[i+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res+=1         
        return 0
