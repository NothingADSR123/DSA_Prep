s="abcabcbb"
d={}
curLen,maxLen=0,0
for i,e in enumerate(s):
    if e in d:
        maxLen=max(curLen,maxLen)
        d={}
        curLen=0
    d[i]=e
    curLen+=1
        
print(maxLen)
print(d)