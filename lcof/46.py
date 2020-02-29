# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 上午10:35
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 46.py
# @Desc    : 说明

class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [1] + [0] * (len(num) - 1)
        for i in range(1, len(num)):
            dp[i] += dp[i - 1]
            if 10 <= int(num[i - 1: i + 1]) <= 25:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.translateNum(12258))
