# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Um very easy solution actually
s = "abc", t = "ahbgdc"
i,j=0,0
while i<len(s) and j < len(t):
    if s[i]==t[j]:
        i+=1
    j+=1
print (True) if len(s)==i else False

# KhudSe kiya hua solution 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        elemLength=0
        while i<len(s):
            while j<len(t):
                if s[i] == t[j]:
                    if i<len(s)-1:
                        i+=1
                    j+=1
                    elemLength+=1
                else:
                    j+=1
            i+=1
        
        if elemLength==len(s):
            return True 
        else:
            return False
        
        