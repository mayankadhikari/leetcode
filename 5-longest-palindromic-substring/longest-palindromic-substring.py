class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ""
        start=0
        max_len=1
        dp=[False]*n
        for i in range(n-1,-1,-1):
            dp[i]=True

            for j in range(n-1,i,-1):
                if s[i]==s[j] and (j-i==1 or dp[j-1]):
                    dp[j]=True
                    if j-i+1>max_len:
                        max_len=j-i+1
                        start=i
                else:
                    dp[j]=False
        return s[start:start+max_len]
        