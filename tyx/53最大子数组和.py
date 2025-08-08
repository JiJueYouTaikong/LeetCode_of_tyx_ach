class Solution:
        def maxSubArray(self, nums):
            '''
            贪心算法(每一步都要保证是局部最优的：即每一步都要维护当前最优)
            1.遍历过程要维护当前累计值及当前局部最大和
            2.当当前累计值已经为负了，则不要再加上当前遍历位置的元素（已经不是最优解了）
            3.而是重新从当前位置重新累计

            O(n)
            O(1)
            '''

            max_sum = -inf
            cur_sum = 0
            n = len(nums)

            for i in range(n):
                if cur_sum < 0 :
                    cur_sum = nums[i] 
                
                else:
                    cur_sum += nums[i]

                max_sum = max(cur_sum, max_sum)
            
            return max_sum
        