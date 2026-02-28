class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=1_000_000_007
        res=0
        for i in range(1,n+1):
            res=((res<<i.bit_length())+i)%mod
        return res