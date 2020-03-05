# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 上午8:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1103.py
# @Desc    : 说明

from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        pos, count, result = 0, 1, [0] * num_people
        while candies != 0:
            count = min(count, candies)
            result[pos] += count
            candies -= count
            pos = (pos + 1) % num_people
            count += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.distributeCandies(7, 4))
    print(solution.distributeCandies(10, 3))
    print(solution.distributeCandies(int(10e9), 3))
