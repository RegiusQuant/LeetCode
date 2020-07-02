# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 上午10:58
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0378.py
# @Desc    : 说明

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            x, y, count = n - 1, 0, 0
            while x >= 0 and y < n:
                if matrix[x][y] <= mid:
                    count += x + 1
                    y += 1
                else:
                    x -= 1
            return count >= k

        left, right, result = matrix[0][0], matrix[-1][-1], matrix[0][0]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
                result = mid
            else:
                left = mid + 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.kthSmallest([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ], 8))
