import random


class Solution:
    def quickselect(self,nums,k):
        '''
        快速选择：若枢轴落位的下标就是想要的len-k，则return，否则或左或右递归partition

        1.主循环进行枢轴划分，得到其最后落位下标
        2.若是，则；否则判断向左或向右递归枢轴划分
        :param nums:
        :param k:
        :return:
        
        T: O(n)
        S: O(1)      递归实现时空间复杂度为 O(logn)   循环（迭代）实现O(1)
        '''

        def partition(nums, left, right):

            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            i = left + 1
            j = right
            while True:
                while i <= j and nums[i] <= pivot:
                    i += 1
                while i <= j and nums[j] > pivot:
                    j -= 1

                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    break

            nums[left], nums[j] = nums[j], nums[left]
            return j

        # 过用例
        # if k == 50000:
        #     return 1

        length = len(nums)
        target_index = length - k

        left,right = 0, length -1
        while left <= right:
            pivot_index = partition(nums,left,right)
            if pivot_index == target_index:
                return nums[pivot_index]
            elif pivot_index < target_index:
                left = pivot_index + 1
            else:
                right = pivot_index - 1


nums = [1,4,7,2,3,5,6]
k = 4

solution = Solution()
print(solution.quickselect(nums,k))



