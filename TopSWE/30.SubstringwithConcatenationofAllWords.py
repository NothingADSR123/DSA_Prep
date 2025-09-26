# Example 1:
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation:
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
# Example 2:
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Explanation:
# There is no concatenated substring.


# Bakwas Question hai BRooo
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        wordLen=len(words[0])
        wordCount=len(words)
        totalLen=wordLen*wordCount
        SuperiorMap={}

        for word in words:
            if word not in SuperiorMap:
                SuperiorMap[word]=0
            SuperiorMap[word]+=1
        res=[]

        for i in range(wordLen):
            left,right=i,i
            seenWords={}
            while right+wordLen <= len(s):
                word=s[right:right+wordLen]
                right+=wordLen

                if word not in SuperiorMap:
                    seenWords.clear()
                    left=right
                else:
                    if word not in seenWords:
                        seenWords[word]=0
                    seenWords[word]+=1

                    while seenWords[word]>SuperiorMap[word]:
                        leftWord=s[left:left+wordLen]
                        seenWords[leftWord]-=1
                        left+=wordLen

                    if right - left == totalLen:
                        res.append(left)
        return res
