# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # words=s.split()
        # l=len(words[-1])
        # return l

        i,length=len(s)-1,0
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            i-=1
            length+=1
        return length