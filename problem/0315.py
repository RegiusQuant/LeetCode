# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 上午9:51
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0315.py
# @Desc    : 说明

class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [0]

        temp = [0] * n
        idxs = [i for i in range(n)]
        result = [0] * n
        self.helper(nums, 0, n - 1, temp, idxs, result)
        return result

    def helper(self, nums, left, right, temp, idxs, result):
        if left == right:
            return

        mid = (left + right) // 2
        self.helper(nums, left, mid, temp, idxs, result)
        self.helper(nums, mid + 1, right, temp, idxs, result)

        if nums[idxs[mid]] <= nums[idxs[mid + 1]]:
            return

        temp[left:right + 1] = idxs[left:right + 1]
        p1, p2 = left, mid + 1
        for i in range(left, right + 1):
            if p1 > mid:
                idxs[i] = temp[p2]
                p2 += 1
            elif p2 > right:
                idxs[i] = temp[p1]
                p1 += 1
                result[idxs[i]] += right - mid
            elif nums[temp[p1]] <= nums[temp[p2]]:
                idxs[i] = temp[p1]
                p1 += 1
                result[idxs[i]] += p2 - mid - 1
            else:
                idxs[i] = temp[p2]
                p2 += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSmaller([5, 2, 6, 1]))
