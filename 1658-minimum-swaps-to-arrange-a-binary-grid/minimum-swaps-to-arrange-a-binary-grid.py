class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        matrix=[]
        n=len(grid)-1
        for row in grid:
            for i in range(n,-1,-1):
                if row[i]==1:
                    break
            matrix.append(n-i)
        swap=0
        while matrix:
            for i ,row in enumerate(matrix):
                if row>=n:
                    break
            if row<n:
                return -1
            swap+=i
            matrix.pop(i)
            n-=1
        return swap
        