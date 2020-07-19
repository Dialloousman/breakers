#https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        islands = 0
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        q = collections.deque()
        
        for r in range (len(grid)):
            for c in range(len(grid[0])):
                
                cell = grid[r][c]
                
                if cell == "1" and (r,c):
                    
                    q.append((r,c))
                    
                    while q:
                        
                        rr,cc = q.pop()
                        
                        grid[rr][cc] = "0"
                    
                        for ds in directions:
                            
                            nR = ds[0] + rr
                            nC = ds[1] + cc
                            
                            if nR >= 0 and nR < len(grid) and nC >= 0 and nC < len(grid[0]):
                                if grid[nR][nC] == "1":
                                    q.append((nR, nC))
                                
                    islands += 1
        return islands