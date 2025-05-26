class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=abs(dividend)
        b=abs(divisor)
        negative=(dividend<0 and divisor>=0) or (dividend>=0 and divisor<0)
        res=0
        while a>=b:
            counter=1
            decre=b
            while a>=decre:
                a-=decre
                res+=counter
                counter+=counter
                decre+=decre
        res=res if not negative else -res
        return min(max(-2**31,res),2**31-1)

        