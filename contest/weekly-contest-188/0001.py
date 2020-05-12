# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 下午8:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target = [0] + target
        result = []
        for i in range(1, len(target)):
            for _ in range(1, target[i] - target[i - 1]):
                result.extend(['Push', 'Pop'])
            result.append('Push')
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildArray([1, 3], 3))
    print(solution.buildArray([1, 2, 3], 3))
    print(solution.buildArray([1, 2], 4))
