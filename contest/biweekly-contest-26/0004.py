# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明


from collections import defaultdict
from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [defaultdict(int) for _ in range(target + 1)]
        dp[0][0] = 0
        result = 0

        for k in range(1, target + 1):
            flag = False

            for i in dp[k - 1].keys():
                for j in range(9):
                    if i + cost[j] > target:
                        continue

                    temp = dp[k - 1][i] * 10 + (j + 1)
                    if temp > dp[k][i + cost[j]]:
                        dp[k][i + cost[j]] = temp
                        flag = True
                        if i + cost[j] == target:
                            result = max(result, dp[k][i + cost[j]])

            if not flag:
                break

        return str(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9))
    print(solution.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12))
    print(solution.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5))
    print(solution.largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], 47))
    print(solution.largestNumber([4, 2, 4, 5, 3, 4, 3, 4, 5], 618))
    print(solution.largestNumber([6, 39, 65, 35, 21, 398, 383, 312, 318], 826))
    print(solution.largestNumber([1, 1, 1, 1, 1, 1, 1, 1, 1], 5000))
