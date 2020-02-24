# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 上午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.strptime(date2, '%Y-%m-%d')
        return abs((d2 - d1).days)


if __name__ == '__main__':
    solution = Solution()
    print(solution.daysBetweenDates("2019-06-29", "2019-06-30"))
    print(solution.daysBetweenDates("2020-01-15", "2019-12-31"))
