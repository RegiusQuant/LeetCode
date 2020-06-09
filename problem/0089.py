# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 上午10:24
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0089.py
# @Desc    : 说明

from typing import List


class Solution:

    def grayCode(self, n: int) -> List[int]:
        result, head = [0], 1
        for i in range(n):
            for j in reversed(range(len(result))):
                result.append(head + result[j])
            head *= 2
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.grayCode(2))
