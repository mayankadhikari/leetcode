class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        l,r=1,x
        sqrt=0
        while l <= r:
            mid=(l+r)//2
            if mid*mid>x:
                r=mid-1
            else:
                sqrt=mid
                l=mid+1
        return sqrt

        