# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 下午8:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mat = [[False] * n for _ in range(n)]
        for u, v in prerequisites:
            mat[u][v] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] and mat[k][j]:
                        mat[i][j] = True

        result = []
        for u, v in queries:
            result.append(mat[u][v])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))
    print(solution.checkIfPrerequisite(2, [], [[0, 1], [1, 0]]))
    print(solution.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]))
    print(solution.checkIfPrerequisite(3, [[1, 0], [2, 0]], [[0, 1], [2, 0]]))
    print(solution.checkIfPrerequisite(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 3], [3, 0]]))
