# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# All the approaches are equally same T-O(n) and S-O(n)
# However O(1) can be approached but NAHHHH too complicated 

class Solution:
    def reverseWords(self, s: str) -> str:
        output=""
        l=s.split()
        for i in range(len(l)-1,-1,-1):
            output+=l[i]
            if i!=0:
                output+=" "
        return output 
    
# ANDDDDDDDDD (CHATGpt wala But I did it properly hi)
def reverseWords(s: str) -> str:
    s = s.strip()  # Remove leading/trailing spaces
    n = len(s)
    result = []
    i = n - 1
    
    while i >= 0:
        while i >= 0 and s[i] == ' ':  # Skip spaces
            i -= 1
        if i < 0:
            break
        j = i
        while j >= 0 and s[j] != ' ':  # Identify a word
            j -= 1
        result.append(s[j + 1:i + 1])  # Add the word
        i = j  # Move to the next word
    
    return " ".join(result)
