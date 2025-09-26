class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] not in "({[" or s[-1] not in ")}]":
            return False
            
        stack=[]

        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            elif i in (')', '}', ']'): 
                if not stack:
                    return False  
                elif  ( i== ')' and stack[-1]=='(' ) or (i== '}' and stack[-1]=='{' )or  (i== ']' and stack[-1]=='[' ):
                    stack.pop()
                
                else:
                    return False
        return len(stack) == 0 
        

