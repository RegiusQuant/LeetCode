# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 下午2:09
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.11.py
# @Desc    : 说明

from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        result = []
        for i in range(k + 1):
            result.append(longer * i + shorter * (k - i))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.divingBoard(1, 2, 3))
