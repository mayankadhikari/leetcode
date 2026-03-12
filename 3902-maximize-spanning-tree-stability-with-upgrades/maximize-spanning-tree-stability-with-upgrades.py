class Solution:
    def maxStability(self,n,edges,k):

        class DSU:
            def __init__(self,n):
                self.p=list(range(n))

            def find(self,x):
                if self.p[x]!=x:
                    self.p[x]=self.find(self.p[x])
                return self.p[x]

            def unite(self,a,b):
                pa=self.find(a)
                pb=self.find(b)
                if pa==pb:
                    return False
                self.p[pb]=pa
                return True

        def check(x):

            dsu=DSU(n)
            used=0

            good=[]
            upgrade=[]

            for u,v,s,m in edges:

                if m==1:
                    if s<x:
                        return False
                    if not dsu.unite(u,v):
                        return False
                    used+=1

                else:
                    if s>=x:
                        good.append((u,v))
                    elif s*2>=x:
                        upgrade.append((u,v))

            for u,v in good:
                if dsu.unite(u,v):
                    used+=1

            up=0
            for u,v in upgrade:
                if up==k:
                    break
                if dsu.unite(u,v):
                    used+=1
                    up+=1

            return used==n-1

        lo,hi,ans=1,200000,-1

        while lo<=hi:
            mid=(lo+hi)//2

            if check(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1

        return ans    