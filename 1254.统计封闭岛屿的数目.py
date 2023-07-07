#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
from typing import List

forward = [[0,1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        res = 0
        for i in range(len(grid)):
            for j in  range(len(grid[0])):
                if (grid[i][j] == 0):
                    if (self.search(grid, i, j)):
                        res += 1
        return res
    
    def search(self, grid, x, y):
        res = True
        grid[x][y] = -1
        for item in forward:
            next_x = x + item[0]
            next_y = y + item[1]
            if(next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0])):
                res = False
            elif(grid[next_x][next_y] == 0):
                flag = self.search(grid, next_x, next_y)
                res = flag if res else res
        
        return res
                
s = Solution()
s.closedIsland([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]])

            
            
            
        
# @lc code=end

