# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        while r >= 0 and c < n:
            if matrix[r][c] == target:
                return True
            if target < matrix[r][c]:
                r -= 1
            else:
                c += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        20
    ))
