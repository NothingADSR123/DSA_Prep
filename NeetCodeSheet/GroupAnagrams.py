# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: ["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
# Example 3:
# Input: strs = [""]
# Output: [[""]]

from typing import List 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # other wise a hashmao that stores key as array of all a-z characters 
        # with count +1 in there spaces
        d={}
        for s in strs:
            array=[0]*26
            for c in s:
                array[ord(c)-ord("a")]+=1
            if tuple(array) not in d:       #to code this part is tough because of syntaxes and rules
                d[tuple(array)]=[]          #not because the sol is hard so chill
            d[tuple(array)].append(s)
        return list(d.values())


        # d={}
        # for i in range(len(strs)):
        #     string="".join(sorted(strs[i]))
        #     if string in d:
        #         d[string].append(strs[i])
        #     else:
        #         d[string]=[strs[i]]
        # return list(d.values())
