# 67. Add Binary
# Easy
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Easy only just a lil confusing coz new thing to think
        res=""
        carry=0
        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            A=int(a[i]) if i<len(a) else 0
            B=int(b[i]) if i<len(b) else 0
            sum=A+B+carry
            carry=sum//2
            ans=sum%2
            res+=str(ans)
        if carry:
            res+=str(1)
        return res[::-1]
