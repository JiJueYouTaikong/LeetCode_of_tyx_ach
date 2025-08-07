from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s):
        '''
        去重后或根本没重时收集并维护最大长度(即：不管进不进行去重，每次循环末尾要维护最大窗口长度)
        如果重复则缩小窗口直至不重复（while循环）

        时间复杂度	O(n)
        空间复杂度	O(k) k为字符种类数（ASCII下可视为 O(1)
        '''
        
        max_length = 0 
        left = 0 

        cnt = defaultdict(int)

        for right,c in  enumerate(s):

            cnt[c] += 1

            while cnt[c] > 1 and left <= right:
                cnt[s[left]] -= 1
                left += 1
            

            max_length = max(max_length, right- left + 1)
        return max_length



s = "abccabaffabcdefgg"
solution = Solution()

print(solution.lengthOfLongestSubstring(s))