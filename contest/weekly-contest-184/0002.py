# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 下午4:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m + 1))
        result = []
        for q in queries:
            result.append(p.index(q))
            p.remove(q)
            p.insert(0, q)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.processQueries([3, 1, 2, 1], 5))
    print(solution.processQueries([4, 1, 2, 2], 4))
    print(solution.processQueries([7, 5, 5, 8, 3], 8))
