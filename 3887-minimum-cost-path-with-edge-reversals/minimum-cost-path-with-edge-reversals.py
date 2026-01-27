import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,2*w))
        dist=[float('inf')]*n
        dist[0]=0
        h=[(0,0)]
        while h:
            d,u=heapq.heappop(h)
            if d!=dist[u]:
                continue
            if u==n-1:
                return d
            for v,w in graph[u]:
                nd=d+w
                if nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(h,(nd,v))
        return -1