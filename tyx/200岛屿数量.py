class Solution:
    def numIslands(self, grid):
        '''
        1.遍历二维矩阵，只要找到任何一个1，立刻维护ans，++
        2.然后立刻调用递归，淹没其自身及上下左右可能存在的“1”

        时间复杂度：O(mn)  遍历
        空间复杂度：O(mn)  最大递归深度
        '''
        m, n = len(grid),len(grid[0])
        ans = 0

        
        def dfs(i,j):
            '''
            dfs(i,j) --> 淹没grid[i][j]上下左右可能的“1”

            边界：i or j不合法或grid[i][j]已为“0”
            递归体：淹没自身及上下左右
            '''

            # 边界
            if i < 0 or i > m-1 or j < 0 or j > n-1 or grid[i][j] == "0":
                return
            
            ### key code
            grid[i][j] = "0"

            # 递归体
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)

        return ans



solution = Solution()

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(solution.numIslands(grid))