# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 上午10:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.13.py
# @Desc    : 说明

from typing import List


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        box.sort()
        dp = [box[i][2] for i in range(len(box))]

        for i in range(len(box)):
            for j in range(i):
                if box[j][0] < box[i][0] and box[j][1] < box[i][1] and box[j][2] < box[i][2]:
                    dp[i] = max(dp[i], dp[j] + box[i][2])
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.pileBox([[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]))
