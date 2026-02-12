class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        res=1
        for i in range(n):
            freq=[0]*26
            dist=0
            maxFreq=0
            for j in range(i,n):
                idx=ord(s[j])-ord('a')
                if freq[idx]==0:
                    dist+=1
                freq[idx]+=1
                maxFreq=max(maxFreq,freq[idx])
                length=j-i+1
                if length==dist*maxFreq:
                    res=max(res,length)
        return res        