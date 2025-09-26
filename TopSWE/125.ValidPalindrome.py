# Example 1
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Brute Force O(n)space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        return filtered == filtered[::-1]

# Two Pointer O(1) space (Khud se did)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        front,back=0,len(s)-1
        while front<back:
            while front<back and not s[front].isalnum():
                front+=1
            while front<back and not s[back].isalnum():
                back-=1
            if s[front].lower() !=s[back].lower():
                return False
            else:
                front+=1
                back-=1
        return True    
            
