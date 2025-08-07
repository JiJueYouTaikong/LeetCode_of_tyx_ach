from functools import cache
class Solution:
    def minDistance(self,word1,word2):
        
        m = len(word1)
        n = len(word2)

        @cache
        def dfs(i,j):
            '''
            dfs(i,j)表示将word1[0-i]变为word2[0-j]所需要的最小次数
            函数体中只有两部分代码：
            1. 递归返回条件（递归边界）
            2. 不同条件下的递归代码（递归体）

            注意：i和j是下标，所以＝0时仍能进行不同条件下的递归处理，所以边界应该是<0
            '''

            # 边界
            if j < 0:   
                return i + 1
            elif i < 0:
                return j + 1
            
            # 情况1：当前字符相同
            if word1[i] == word2[j]:
                return dfs(i-1,j-1)
            

            # 情况2：当前字符不同，取代价最小的那个
            return min(dfs(i-1,j),dfs(i,j-1),dfs(i-1,j-1)) + 1
        
        return dfs(m-1,n-1)
 

word1 = "horse"
word2 = "rose"

solution = Solution()
print(solution.minDistance(word1,word2))