from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row=len(grid)
        col=len(grid[0])
        count=0
       
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    count+=1
                    q=deque()
                    q.append((r,c))
                    grid[r][c]=0
                    while q:
                        x,y=q.popleft()
                        dir=[(-1,0),(1,0),(0,-1),(0,1)]
                        for nx,ny in dir:
                            dx=x+nx
                            dy=y+ny
                            if (0<=dx<row and 0<=dy<col )and grid[dx][dy]=="1":
                            
                                grid[dx][dy]=0
                                q.append((dx,dy))
        return count
                



        
        